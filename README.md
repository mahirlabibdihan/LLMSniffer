<div align="center">

<h1>LLMSniffer: LLM Generated  Code Detection</h1>

**[Mahir Labib Dihan](https://mahirlabibdihan.github.io/)** · **[Abir Muhtasim](https://abir66.github.io/)** 

Department of Computer Science and Engineering <br>
Bangladesh University of Engineering and Technology (BUET)

Email: [mahirlabibdihan@gmail.com](mailto:mahirlabibdihan@gmail.com), [auntor505@gmail.com](mailto:auntor505@gmail.com)
</div>


## Abstract

The increasing prevalence of Large Language Models (LLMs) in generating code has made distinguishing AI-generated code from human-written code a critical challenge. To address this, we introduce **LLMSniffer**, a robust detection framework that leverages **GraphCodeBERT**, fine-tuned using **supervised contrastive learning**. Utilizing benchmark datasets such as **GPTSniffer** and  **Whodunit**, LLMSniffer achieves notable improvements in detection accuracy, increasing from **70%** to **78%** on GPTSniffer and from **91%** to **94%** on Whodunit. By combining the representational power of GraphCodeBERT with the discriminative strength of contrastive learning, LLMSniffer provides a state-of-the-art solution for detecting LLM-generated code, ensuring greater transparency and accountability in software development.

![Overview](overview.png)

## Demontration

Check out the [live demo](https://huggingface.co/spaces/mahirlabibdihan/LLMSniffer) and [demo video](https://youtu.be/xkb_vrEfJIY) of LLMSniffer.

![Demo](streamlit.png)

## GPTSniffer

- Paper: [GPTSniffer](https://www.sciencedirect.com/science/article/pii/S0164121224001043)
- Train data: [GPTSniffer-Train](data/gptsniffer/train/)
- Test data: [GPTSniffer-Test](data/gptsniffer/test/)
- Checkpoint: [GPTSniffer-Checkpoint](https://huggingface.co/mahirlabibdihan/LLMSniffer/blob/main/gptsniffer.pth)

<div align="center">

| Metric       | GPTSniffer | Ours (LLMSniffer) |
|--------------|:----------:|:-----------------:|
| Accuracy     | 70.33%     | 77.66%            |
| Precision    | 90.32%     | 80.70%            |
| Recall       | 42.75%     | 70.23%            |
| F1 Score     | 58.03%     | 75.10%            |

</div>

**Test Set Embedding Visualization:**

<table>
    <tr>
        <th align="center">
            GPTSniffer
        </th>
        <th align="center">
            LLMSniffer
        </th>
    </tr>
  <tr>
    <td align="center">
      <img src="tsne_1.png" alt="GPTSniffer" style="width: 100%;">
    </td>
    <td align="center">
      <img src="tsne_2.png" alt="LLMSniffer" style="width: 100%;">
    </td>
  </tr>
</table>

## Whodunit

- Paper: [Whodunit](https://arxiv.org/pdf/2403.04013)
- Train data: [Whodunit-Train](data/whodunit/train/)
- Test data: [Whodunit-Test](data/whodunit/test/)
- Checkpoint: [Whodunit-Checkpoint](https://huggingface.co/mahirlabibdihan/LLMSniffer/blob/main/whodunit.pth)

<div align="center">

| Metric       | Whodunit | Ours (LLMSniffer) |
|--------------|:--------:|:-----------------:|
| Accuracy     | 91%      | 94.65%            |
| Precision    | 91%      | 94.94%            |
| Recall       | 91%      | 94.34%            |
| F1 Score     | 91%      | 94.64%            |

</div>