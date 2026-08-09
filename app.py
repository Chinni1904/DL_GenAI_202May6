import streamlit as st
import torch
import torch.nn.functional as F
import pandas as pd

from model import load_model

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Smart MCQ Solver",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load model 
with st.spinner("Loading AI model..."): 
    tokenizer, model = load_model() 

#Answer labels 
labels = ["A", "B", "C", "D", "E"]

# ------------------------------------
# Prediction Function
# ------------------------------------

def predict_top3(question, options):

    labels = ["A", "B", "C", "D", "E"]

    scores = []

    with torch.no_grad():

        for option in options:

            text = question + " </s> " + option

            inputs = tokenizer(
                text,
                return_tensors="pt",
                truncation=True,
                padding=True,
                max_length=256
            )

            outputs = model(**inputs)

            probability = F.softmax(
                outputs.logits,
                dim=1
            )[0][1].item()

            scores.append(probability)

    ranking = sorted(
        zip(labels, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranking
# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🧠 Smart MCQ Solver")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📝 Predict",
        "📊 Model Performance",
        "ℹ️ About"
    ]
)

# -----------------------------
# Home Page
# -----------------------------
if page == "🏠 Home":

    st.title("🧠 Smart MCQ Solver")

    st.markdown("---")

    st.header("Project Overview")

    st.write("""
This application predicts the **Top-3 most probable answers**
for a Multiple Choice Question using a fine-tuned
**RoBERTa Sequence Classification Model**.

The project was developed as part of the
**IIT Madras Diploma in Data Science – Deep Learning Project**
and submitted for the Kaggle **Smart MCQ Solver Challenge**.
""")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Dataset")

        st.write("""
- Training Samples : **2000**
- Test Samples : **500**
- Answer Choices : **A, B, C, D, E**
""")

    with col2:

        st.subheader("Technologies Used")

        st.write("""
- Python
- PyTorch
- Hugging Face Transformers
- RoBERTa
- Streamlit
- Scikit-learn
- Weights & Biases
""")

# -----------------------------
# Prediction Page
# -----------------------------
# -----------------------------
# Prediction Page
# -----------------------------
elif page == "📝 Predict":

    st.title("🧠 Smart MCQ Solver")

    st.markdown(
        """
Enter a **Question** and all five answer options.

The model will rank the **Top-3 most probable answers**.
"""
    )

    st.divider()

    question = st.text_area(
        "Question",
        height=120
    )

    optionA = st.text_area("Option A")
    optionB = st.text_area("Option B")
    optionC = st.text_area("Option C")
    optionD = st.text_area("Option D")
    optionE = st.text_area("Option E")

    if st.button(
        "🚀 Predict Top 3",
        use_container_width=True
    ):

        if (
            question.strip() == ""
            or optionA.strip() == ""
            or optionB.strip() == ""
            or optionC.strip() == ""
            or optionD.strip() == ""
            or optionE.strip() == ""
        ):

            st.warning(
                "Please fill all fields."
            )

        else:

            options = [
                optionA,
                optionB,
                optionC,
                optionD,
                optionE
            ]

            ranking = predict_top3(
                question,
                options
            )

            option_dict = {

                "A": optionA,

                "B": optionB,

                "C": optionC,

                "D": optionD,

                "E": optionE

            }

            st.divider()

            st.success(
                f"🏆 Best Prediction : Option {ranking[0][0]}"
            )

            st.subheader("Top 3 Predictions")

            medals = [

                "🥇",

                "🥈",

                "🥉"

            ]

            for i in range(3):

                label, score = ranking[i]

                st.markdown(
                    f"### {medals[i]} Option {label}"
                )

                st.progress(score)

                st.write(
                    f"**Confidence : {score:.2%}**"
                )

                with st.expander(
                    "View Option"
                ):

                    st.write(
                        option_dict[label]
                    )

                st.markdown("---")

# -----------------------------
# Performance Page
# -----------------------------
elif page == "📊 Model Performance":

    import pandas as pd

    results = pd.DataFrame({

        "Model":[

            "TF-IDF",

            "Sentence Transformer",

            "RoBERTa"

        ],

        "MAP@3":[

            0.74355,

            0.42227,

            0.75270

        ]

    })

    st.dataframe(
        results,
        use_container_width=True
    )

    st.bar_chart(
        results.set_index("Model")
    )

# -----------------------------
# About Page
# -----------------------------
else:

    st.title("ℹ️ About")

    st.write("""
**Project Name**

Smart MCQ Solver Challenge

**Student**

Raja Manasa Yerramreddy

**Institute**

Indian Institute of Technology Madras

**Course**

Diploma in Data Science

**Project**

Deep Learning
""")