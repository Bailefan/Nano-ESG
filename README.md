### Nano-ESG: Extracting Corporate Sustainability Information from News Data

This is the supplementary material for the paper [Nano-ESG: Extracting Corporate Sustainability Information from News Data](https://arxiv.org/abs/2412.15093).

In order to run the notebooks, we recommend creating a new environment with python=3.10 . Then, you can install the packages in the requirements.txt file using

```
pip install -r requirements.txt
```


#### In the supplementary material, you will find

1. The data
    - **evaluation_data**: The annotated datasets as described in Section 5 of the paper
    - **full_data**: The full dataset as described in Section 4 of the paper
2. The Evaluation Guidelines (*Note that the guidelines were originally in German and translated to English by us for this paper*):
    - **summary_evaluation.md**: Guidelines for the first evaluation task
    - **sentiment_aspect_evaluation.md**: Guidelines for the second evaluation task
3. The prompts given to the LLMs:
    - **first_filter_prompt.md**: The prompt for the first LLM filter step (Section 3.4)
    - **final_prompt.md**: The final prompt to extract the ESG information from each news article (Section 3.6)
4. Notebooks to replicate results in the paper:
    - **evaluate_task1.ipynb**: This notebook replicates the results we present in Section 5.2
    - **evaluate_task2.ipynb**: This notebook replicates the results we present in Section 5.3 and Section 6.2
    - **investigate_data.ipynb**: This notebook replicates the results we present in Section 4 and Section 6.1
    - **explore_topics.ipynb**: This notebook replicates the results we present in Section 6.3. In addition, it is possible to explore other interesting topics.
