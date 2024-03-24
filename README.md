# 39_PAA_01

Here we are working on ps 1 which is 'AI content Authenticity challenge' .
steps followed :

1. literature and research paper analysis.
2. Data extraction from kaggle
   dataset : chatgpt_paraphrases.csv (https://www.kaggle.com/code/naifislam/differentiating-text-generated-from-human-and-ai/input?select=chatgpt_paraphrases.csv)

3. Data preprocessing:
   1. Vectorizing text using TfidfVectorizer
   2. converting output of TfidfVectorizer to array , that can be given to model
4. Using sklearn model Random Forest and getting the accuracy of 96.5%

5. Fitting all the processed data to above models

 ![Output1](https://github.com/PrashantBarai/39_PAA_01/assets/144236026/c29479f8-790a-492f-9da6-3a5ec68a3f0b)

 ![Output2](https://github.com/PrashantBarai/39_PAA_01/assets/144236026/1990a40e-bc7e-4222-9fc6-f73a8d772a52)

 ![Output3(Confusion Matix Obtained)](https://github.com/PrashantBarai/39_PAA_01/assets/144236026/5885ed41-6a8c-478b-8f87-1cc1c4ac7cb2)


6. Started making new Model through keras .

7. Fit train data to new model.
