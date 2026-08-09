




Mon, Jun 29 at 10:25 PM
May 2026 Kaggle competition

Overview
Welcome to the Smart MCQ Solver Challenge!

In this competition, participants are required to build machine learning or AI based systems capable of solving complex multiple choice questions. Each question contains a prompt along with five possible answer options labeled A, B, C, D, and E. The objective is to predict the top three most likely correct answers in ranked order.

The challenge focuses on evaluating a model’s ability to understand context, reason across options, and rank answers effectively. Participants are encouraged to experiment with a variety of approaches including transformer architectures, retrieval based pipelines, fine tuned language models, ensemble strategies, and efficient inference techniques.

Submissions will be evaluated using Mean Average Precision at 3 (MAP@3), where models receive higher scores when the correct answer appears earlier in their ranked predictions.

This competition is designed to encourage experimentation in natural language understanding, reasoning, and intelligent answer ranking while promoting efficient and reliable AI solutions.

Goal: The goal of this competition is to build intelligent models that can accurately predict the top three most probable answers for challenging multiple choice questions. Participants are encouraged to develop efficient AI and machine learning solutions capable of strong reasoning and answer ranking.

Start

a month ago
Close

19 days to go
Description
Multiple choice question answering remains an important benchmark for evaluating reasoning, language understanding, and answer ranking capabilities of modern AI systems. In many real world scenarios, intelligent models must not only identify the correct answer but also rank alternative answers effectively based on confidence and contextual understanding.

In this competition, participants are provided with a collection of challenging MCQ style questions. Each question includes a prompt along with five possible answer choices labeled A, B, C, D, and E. The task is to predict the top three most probable correct answers for every question.

The competition is designed to encourage experimentation with a variety of approaches including transformer based models, retrieval augmented systems, fine tuned language models, prompt engineering, ensemble methods, and efficient inference pipelines.

Submissions are evaluated using Mean Average Precision at 3 (MAP@3), which rewards models that rank the correct answer higher in their predictions. Successful solutions should demonstrate strong reasoning ability, robust generalization, and effective answer ranking performance across diverse question patterns and difficulty levels.

Evaluation
Evaluation
Submissions are evaluated using Mean Average Precision at 3 (MAP@3).

For each question, participants must predict up to three answer labels in ranked order from the available options: A, B, C, D, and E. Models receive higher scores when the correct answer appears earlier in the prediction list.

Example:

If the correct answer is:

A
Then the following predictions would receive:

A B C   → highest score
B A C   → Relatively lower score
C D A   → lowest score
Submission Format
For every question ID in the test set, submissions must contain exactly three predicted labels separated by spaces.

Example:

ID,Prediction
1,A B C
2,C A D
3,B D A

Dataset Description
Dataset Description
The dataset for this competition consists of multiple choice questions designed to evaluate reasoning, comprehension, and answer ranking capabilities of AI systems. Each question contains a prompt along with five answer choices labeled A, B, C, D, and E.

Participants are provided with a training dataset containing questions and their corresponding correct answers. The test dataset contains similar questions without the answer column, and participants must predict the top three most probable answers for each question.

The dataset includes a variety of question styles and difficulty levels to encourage models that generalize effectively across different problem types.

Files
train.csv Contains the training questions along with the correct answer labels.

test.csv Contains the test questions without answers. Participants must generate predictions for this file.

sample_submission.csv Demonstrates the correct submission format for the competition.

Columns
id Unique identifier for each question.

prompt The question or problem statement.

A, B, C, D, E The five possible answer choices.

answer The correct answer label in the training dataset. This column is not present in the test dataset.

Attached image is the folder structure of my data

Below given is head of my data
	id	prompt	A	B	C	D	E	answer
0	1	Pick the best possible answer: What is Martin ...	Martin Heidegger believes that humans exist wi...	Martin Heidegger believes that humans do not e...	Martin Heidegger does not believe in the exist...	Martin Heidegger believes that the relationshi...	Martin Heidegger believes that time is an illu...	B
1	2	What is accelerator-based light-ion fusion?	Accelerator-based light-ion fusion is a techni...	Accelerator-based light-ion fusion is a techni...	Accelerator-based light-ion fusion is a techni...	Accelerator-based light-ion fusion is a techni...	Accelerator-based light-ion fusion is a techni...	A
2	3	Determine the correct option: What is the term...	Blueshifting	Redshifting	Reddening	Whitening	Yellowing	C
3	4	Select the most accurate option: What is Marti...	Martin Heidegger believes that humans exist wi...	Martin Heidegger believes that humans do not e...	Martin Heidegger does not believe in the exist...	Martin Heidegger believes that the relationshi...	Martin Heidegger believes that time is an illu...	B
4	5	Identify the correct statement: What is the co...	Simultaneity is relative, meaning that two eve...	Simultaneity is relative, meaning that two eve...	Simultaneity is absolute, meaning that two eve...	Simultaneity is a concept that applies only to...	Simultaneity is a concept that applies only to...	A

Consider you are a machine learning student and you are supposed to submit the competition and you have to push all the updates in github repository and provide report of the project

Your report should clearly explain the models you used, including diagrams and architecture details. Describe your training process, dataset splits, any data augmentation, and the overall pipeline. Include hyperparameter tuning details with logs or trial results. Present evaluation metrics relevant to your task, with tables or plots. Finally, provide error analysis with examples of model failures and insights drawn from them.

This is the mile stone plan as per the course 
Milestone 0

Jun 22, 2026


Thursday


Orientation & Setup

Attend the orientation session.
Create accounts on Kaggle, GitHub, and Weights & Biases (W&B).
Verify environment setup and tools access.
Milestone 1

Jun 24, 2026


Wednesday


NLP Foundation & Semantic Similarity

Perform Text cleaning, tokenization, and handling missing data.
Generate embeddings using baseline models like TF-IDF and Word2Vec.
Compute cosine similarity between a 'prompt' and 'options' and understand its concepts.
Calculate mAP@3 and understand the concept of mAP.
Milestone 2

Jul 1, 2026


Wednesday


Enter the Transformers

Introduction to the Hugging Face transformers and datasets libraries.
Learn architecture of BERT/RoBERTa and the concept of attention mechanisms.
Use pre-trained embedding models to generate context-aware embeddings.
Zero-shot classification concepts with transformers and SLMs
Milestone 3

Jul 8, 2026


Wednesday


Context Augmentation with RAG Pipelines

The limitations of General LLMs. Learn the RAG pipeline in brief.
Loading a simple pre-built vector database.
Retrieving external context based on the question prompt.
Feeding the retrieved context + prompt + choices into the model to improve reasoning.
Milestone 4

Jul 15, 2026


Wednesday


Formulating MCQ Task & Fine-Tuning

Data formatting for MCQ: Concatenating the question with options.
Introduction to LoRA-finetuning, and its advantages over Full-finetuning.
Setting up a training loop to fine-tune the model weights on the dataset.
Managing GPU memory and batch sizes.
Training efficiency strategies with Training arguments.
Milestone 5

Jul 21, 2026


Wednesday

Ensembling

Extracting and sorting logits to get the top 3 predictions (e.g., A C B).
Ensemble techniques to stack predictions from multiple models.
Other strategies to improve predictions.
Last Submission

26-07-2026


Sunday

Final Submission & Presentation

Make final Kaggle submission.
Create report & Present results and analysis (Macro F1, Error Analysis, Insights).
Optional: Deploy model using Streamlit/Gradio.

Follow the below criteria
Students must meet the following requirements:

Model Requirements

Present at least three unique models:
One model built from scratch
One pretrained model
One additional model of choice
Experiment Tracking

All models must have valid Weights & Biases (WandB) runs
At least three runs must be compared using common evaluation metrics such as accuracy and F1 score
Development Practice

GitHub commit history must reflect consistent progress over more than three weeks
Last-minute uploads without meaningful commit history will not be accepted

A minimum score cutoff of <<0.73>> is required in the final Kaggle submission to qualify for the viva

Is there anything that needs to be changed based on the recent changes I made in this snippet

Thu, Jul 23 at 9:07 PM

dl-23ds3000191-notebook-t22026.ipynb
File
These are the scores of my 3 models,

submission_tfidf : 0.74355
submission_sentence_transformer : 0.42227
submission_roberta : 0.75270

Attached is my code
consider you are a student and write a report on the project and observations at each stage 

image(20260808-170931).png


Pasted text(20260809-172154).txt
Document

Excellent! Now we'll build Part 2, which is the core of your application—loading your fine-tuned RoBERTa model and creating the prediction function that matches your Kaggle notebook.

Step 1: Update Imports
Replace the imports at the top of app.py with:

import streamlit as st
import torch
import torch.nn.functional as F

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)
Step 2: Load Model
Add this immediately after st.set_page_config().

# -------------------------------
# Load Model
# -------------------------------

MODEL_PATH = "model"

@st.cache_resource
def load_model():

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_PATH
    )

    model.eval()

    return tokenizer, model


tokenizer, model = load_model()
Why @st.cache_resource?
Without it, Streamlit reloads the RoBERTa model every time the page refreshes.

With caching:

Loads once

Faster predictions

Lower memory usage

Step 3: Labels
Below the above code:

labels = ["A", "B", "C", "D", "E"]
Step 4: Prediction Function
This follows the same pairwise inference that you used in Kaggle.

# ------------------------------------
# Prediction Function
# ------------------------------------

def predict_top3(question, options):

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

            logits = outputs.logits

            probability = F.softmax(
                logits,
                dim=1
            )[0][1].item()

            scores.append(probability)

    ranking = sorted(

        zip(labels, scores),

        key=lambda x: x[1],

        reverse=True

    )

    return ranking
This function:

Takes Question

Takes 5 options

Predicts each pair individually

Computes probability of class 1 (Correct Answer)

Returns:

[
 ('B',0.94),
 ('D',0.78),
 ('A',0.52),
 ('C',0.34),
 ('E',0.18)
]
Step 5: Update the Predict Page
Replace your existing:

elif page == "📝 Predict":
section with:

elif page == "📝 Predict":

    st.title("🧠 Smart MCQ Solver")

    question = st.text_area(
        "Enter Question"
    )

    col1, col2 = st.columns(2)

    with col1:

        optionA = st.text_area("Option A")

        optionB = st.text_area("Option B")

        optionC = st.text_area("Option C")

    with col2:

        optionD = st.text_area("Option D")

        optionE = st.text_area("Option E")

    if st.button("Predict Top 3"):

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

        st.success("Prediction Completed")

        st.subheader("Top 3 Predictions")

        medals = ["🥇", "🥈", "🥉"]

        for i in range(3):

            label, score = ranking[i]

            st.write(

                f"{medals[i]} **{label}**"

                f" &nbsp;&nbsp;&nbsp;"

                f"Confidence : **{score:.4f}**"

            )
Expected Output
When the user enters:

Question

Option A

Option B

Option C

Option D

Option E
and clicks Predict Top 3, the output will look like:

🥇 B    Confidence: 0.9342

🥈 D    Confidence: 0.8241

🥉 A    Confidence: 0.6023
Folder Structure
DL_GENAI_T2_2026/

│
├── app.py
├── model/
│      config.json
│      model.safetensors
│      tokenizer.json
│      tokenizer_config.json
│
├── requirements.txt
└── README.md
Before moving to Part 3
Run the app:

streamlit run app.py
Test it with any sample question from your dataset.

If the model loads and predictions are displayed correctly, we'll move to Part 3, where we'll enhance the interface by:

displaying the actual option text (not just labels A–E),

showing a confidence bar for each prediction,

adding a cleaner, professional layout suitable for your IIT Madras project demonstration.


Part 3

Great! Now we'll make the application look like a professional AI application instead of a simple prediction page.

In Part 3, we'll:

Improve the UI

Show the actual predicted option text (instead of only A, B, C)

Display confidence bars

Highlight the best prediction

Add expandable sections for readability

Replace the entire Prediction Page
Replace your current:

elif page == "📝 Predict":
section with the following.

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
What changed?
Instead of this:

🥇 B

Confidence : 0.92
You'll now see:

🏆 Best Prediction : Option B

🥇 Option B

███████████████████████ 92%

Confidence : 92%

▼ View Option

The complete answer text...

-----------------------
User Experience
The application now:

✅ validates input

✅ displays confidence percentages

✅ shows progress bars

✅ displays the actual predicted option

✅ highlights the best prediction

Home Page Enhancement
Below your Project Overview, add:

st.info(
    """
**Best Kaggle Score**

🥇 RoBERTa : **0.75270**

Baseline TF-IDF : **0.74355**
"""
)
Performance Page Enhancement
Replace your table with:

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
This gives you both an interactive table and a bar chart comparing the three models.

Current Progress
You now have:

✅ Multi-page Streamlit application

✅ RoBERTa model loading

✅ MCQ prediction page with Top-3 ranking

✅ Confidence scores and progress bars

✅ Performance dashboard

Next (Part 4)
We'll transform the app into a polished portfolio project by adding:

🎨 Custom CSS for a modern UI

📈 Probability distribution chart for all five options

📜 Prediction history (stored during the session)

📥 Download predictions as CSV

📱 Responsive layout

🤗 Final configuration for deployment on Hugging Face Spaces

This final step will make the application look much more professional and presentation-ready.


Now deploy in Hugging face

Perfect! Since your Streamlit app is ready and your RoBERTa model loads successfully, the final step is deploying it on Hugging Face Spaces.

Step 1: Create a GitHub Repository
Create a new repository named:

smart-mcq-solver
Your project structure should look like:

smart-mcq-solver/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   ├── special_tokens_map.json
│   ├── vocab.json
│   ├── merges.txt
│   └── training_args.bin
│
└── assets/
    ├── logo.png
    └── banner.png
Step 2: Create requirements.txt
Create requirements.txt

streamlit==1.47.1
torch
torchvision
transformers==4.55.4
tokenizers
safetensors
sentencepiece
numpy
pandas
scikit-learn
Step 3: Create README.md
# 🧠 Smart MCQ Solver

## Overview

This project predicts the **Top-3 answers** for Multiple Choice Questions using a fine-tuned **RoBERTa Sequence Classification Model**.

---

## Project Details

**Course**

IIT Madras Diploma in Data Science

Deep Learning Project

---

## Kaggle Competition

Smart MCQ Solver Challenge

---

## Models Compared

| Model | MAP@3 |
|-------|-------|
| TF-IDF | 0.74355 |
| Sentence Transformer | 0.42227 |
| RoBERTa | **0.75270** |

---

## Technologies

- Python
- PyTorch
- HuggingFace Transformers
- Streamlit
- Weights & Biases

---

## Author

Raja Manasa Yerramreddy
Step 4: Create .gitignore
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
.venv/
Step 5: Push to GitHub
git init

git add .

git commit -m "Initial Streamlit App"

git branch -M main

git remote add origin https://github.com/<your_username>/smart-mcq-solver.git

git push -u origin main
Step 6: Create Hugging Face Space
Go to

👉 https://huggingface.co/new-space

Fill the details:

Owner

Your Account

Space Name

smart-mcq-solver
License

MIT

SDK

✅ Streamlit

Hardware

CPU Basic (Free)

Visibility

Public

Click

Create Space
Step 7: Upload Project
You have two options.

Option 1 (Recommended)
Connect the Hugging Face Space to your GitHub repository.

Every GitHub push will automatically redeploy the app.

Option 2
Drag and drop:

app.py

requirements.txt

README.md

model/

assets/
Step 8: Wait for Build
Hugging Face will display:

Building...
After approximately 2–5 minutes, it should change to:

Running
Step 9: Your App URL
It will be available at:

https://huggingface.co/spaces/<username>/smart-mcq-solver
or

https://<username>-smart-mcq-solver.hf.space
If Deployment Fails
Go to:

Logs
Look for errors such as:

ModuleNotFoundError
Tokenizer not found
CUDA unavailable
or

RuntimeError
Copy the logs and I can help you troubleshoot them.

Optional: Improve the Home Page
To make the application more polished, add a banner image in assets/ and display it at the top of your home page:

from PIL import Image

image = Image.open("assets/banner.png")
st.image(image, use_container_width=True)
You can also show key project metrics using Streamlit's metric widgets:

col1, col2, col3 = st.columns(3)

col1.metric("Best MAP@3", "0.75270")
col2.metric("Models Compared", "3")
col3.metric("Dataset", "2,000 Train / 500 Test")
Recommended Final Project Structure
smart-mcq-solver/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   ├── special_tokens_map.json
│   ├── vocab.json
│   ├── merges.txt
│   └── training_args.bin
│
└── assets/
    ├── banner.png
    └── logo.png
This setup is clean, reproducible, and ready for both GitHub and Hugging Face Spaces. Once you deploy it, we can also refine the UI and add features such as prediction history, downloadable results, or confidence visualizations if you want to enhance it further.


