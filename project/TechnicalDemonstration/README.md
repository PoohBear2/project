# Technical Demonstration 

- submodule: deepslide (https://github.com/BMIRDS/deepslide.git)

## Introduction:

In this project, you will be given a small histology dataset and use it to demonstrate your data processing and deep learning skills in Python. The project aims to highlight the importance of these skills in medical deep learning research. You will be expected to preprocess and analyze the data, and train a deep learning model using Python.

To easily share and track your work, consider cloning this repository and creating a private repository. This will give you full control over the repository and ensure that your work is secure. After cloning the repository, add Saeed (`saeedhassanpour`) and Naofumi (`ntomita`) as collaborators with a read-role so that we can access and review your work. 

## Environment setup:

To complete this project, you will need to set up your environment with the required packages. Start by reading the DeepSlide's README for instructions on how to install the necessary packages. You can also find a setup script in the `scripts` folder if you prefer to use a container. Follow the instructions carefully to ensure that your environment is properly set up and ready for data processing and deep learning tasks.

## Data processing: 

The first step in preprocessing the dataset is to download it from Dropbox and unzip it. Then, write a script to copy the slides data to the `wsi` folder in a format that the `scripts/generate_patches.py` script can process. This script should take the slides data folder and the meta file `data/partition.csv` as inputs.

[Dataset Link](https://www.dropbox.com/s/lpojnw7h0tz9pjc/tcga_renal_small.zip)

In the second stage, use the `generate_patches.py` script to generate patches for model training. This script replaces the `code/2_process_patches.py` script to reduce computational requirements. Be sure to implement any values indicated as `REPLACE_WITH_ACTUAL_VALUE` in the script.

## Model training: 

The model training stage involves using the `code/3_train.py` script to train a deep learning model on the preprocessed dataset. To ensure proper training, it is important to read the DeepSlide readme and source code to set the appropriate flags.

It is important to keep in mind that all hyperparameters are subject to change in order to improve the performance of the model. When training the model, be prepared to experiment with different hyperparameter values and make adjustments as necessary. 

## Model evaluation: 

To determine the best performing model, use the validation set for evaluation. This will allow you to compare the performance of different models and select the one that performs the best. When evaluating the models, consider using various metrics to get a comprehensive understanding of their performance.

## Reporting: 

In the reporting stage, provide a brief summary of the following aspects of your project:

1. Model Evaluation and Analysis: Present a thorough evaluation of the model's performance, including the metrics used to assess its performance and a detailed analysis of the results.

2. Design Choices and Reasoning: Explain the design choices you made and the reasoning behind them, as well as any options you tried during the model development process.

3. Performance Improvement Suggestions: Offer suggestions on how to improve the model's performance, including any changes that could be made to the model architecture or training process.

4. (if any) Improvement Suggestions for DeepSlide Library: Provide suggestions for improvements that could be made to the DeepSlide library (or any scripts provided) to enhance its functionality and usability for future projects. If you have already implemented such improvements, please indicated those here.

Please add your report to your repository in markdown format.

