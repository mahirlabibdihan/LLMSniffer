<div align="center">

<h1>LLMSniffer: LLM Generated  Code Detection</h1>

[**Mahir Labib Dihan**](https://mahirlabibdihan.github.io/) · [**Abir Muhtasim**](https://abir66.github.io/)

Department of Computer Science and Engineering 
Bangladesh University of Engineering and Technology (BUET)

Email: [mahirlabibdihan@gmail.com](mailto:mahirlabibdihan@gmail.com), [auntor505@gmail.com](mailto:auntor505@gmail.com)
</div>


## Abstract

The increasing prevalence of Large Language Models (LLMs) in generating code has made distinguishing AI-generated code from human-written code a critical challenge. To address this, we introduce **LLMSniffer**, a robust detection framework that leverages **GraphCodeBERT**, fine-tuned using **supervised contrastive learning**. Utilizing benchmark datasets such as [GPTSniffer](https://www.sciencedirect.com/science/article/pii/S0164121224001043) and  [Whodunit](https://arxiv.org/pdf/2403.04013), LLMSniffer achieves notable improvements in detection accuracy, increasing from **70%** to **78%** on GPTSniffer and from **91%** to **94%** on Whodunit. By combining the representational power of GraphCodeBERT with the discriminative strength of contrastive learning, LLMSniffer provides a state-of-the-art solution for detecting LLM-generated code, ensuring greater transparency and accountability in software development.

![Overview](overview.png)

## GPTSniffer

- Paper: [GPTSniffer](https://www.sciencedirect.com/science/article/pii/S0164121224001043)
- Train data: [GPTSniffer-Train](data/gptsniffer/train/)
- Test data: [GPTSniffer-Test](data/gptsniffer/test/)
- Checkpoint: [GPTSniffer-Checkpoint](https://huggingface.co/mahirlabibdihan/LLMSniffer/blob/main/gptsniffer.pth)
- Accuracy increased from 70% to 78%

## Whodunit

- Paper: [Whodunit](https://arxiv.org/pdf/2403.04013)
- Train data: [Whodunit-Train](data/whodunit/train/)
- Test data: [Whodunit-Test](data/whodunit/test/)
- Checkpoint: [Whodunit-Checkpoint](https://huggingface.co/mahirlabibdihan/LLMSniffer/blob/main/whodunit.pth)
- Accuracy increased from 91% to 94%
