# Data Synthesizer

One of the biggest obstacles in many fields machine learning, whether it is classification, natural language processing, etc, is finding or creating data to suit your training needs. 
There are hundreds of thousands of datasets on sites like Kaggle or HuggingFace, but sometimes, you are working on a more niche projecct that might require more specific data to train your model.
Recently, generative AI like chatbots have been explored as possible sources of synthetic data. Simiarly, transformer models have been trained to spit out similar data given samples. 


While working on my emotional medical response chatbot, I realized that I wanted a dataset that was different than what I could find. 


In this shorter project, I developed a way to synthesize data through the use of the Google Studio AI API. 


However, there were a few problems with generative AI.
1. As you generate more and more, the quality of responses decrease, which means the dataset becomes more repetitive, nonsensical, and low quality
2. Your prompting needs to be specific and easily understood
3. You need to parse your data for problems, process them, and then spit out a clean dataset


If these problems aren't addressed, you will end up with a dataset that will not be fit for training, resulting in high loss, especially in the evaluation stage.
By combining the power of pandas and regex, we can create a powerful pipeline from a single prompt to a working dataset.
The data synthesizer was used for my mediresponse project, but it can be changed to be used for any project.


Key parts:
1. There is a file named sample.csv. This is where you will first introduce some high quality data that you want to be similar to the rest of your dataset.
2. Replace necessary path files for where your output data should go. For instance, for my mediresponse project, I wanted to create directories for each emotion a relative/friend of a patient might have
3. Add more processing as needed in the process.py file
