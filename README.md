<h1 align="center">AI GENERATED  CODE DETECTION</h1>

![Overview](overview.png)

## Overview

This repository contains the code for the project of the course CSE 472: Machine Learning Sessional. The project is about improving the performance of the existing models for the task of authorship attribution. The models that are improved are GPTSniffer and WhodUnit. The models are improved by using ensemble learning techniques. The models are trained on the PAN 2013 dataset.

## GPTSniffer

- Paper: [GPTSniffer](https://www.sciencedirect.com/science/article/pii/S0164121224001043)
- Train data: [GPTSniffer-Train](data/gptsniffer/train/)
- Test data: [GPTSniffer-Test](data/gptsniffer/test/)
- Checkpoint: [GPTSniffer-Checkpoint](https://huggingface.co/mahirlabibdihan/LLMSniffer/blob/main/gptsniffer.pth)
- Accuracy increased from 70% to 78%

## WhodUnit

- Paper: [Whodunit](https://arxiv.org/pdf/2403.04013)
- Train data: [Whodunit-Train](data/whodunit/train/)
- Test data: [Whodunit-Test](data/whodunit/test/)
- Checkpoint: [Whodunit-Checkpoint](https://huggingface.co/mahirlabibdihan/LLMSniffer/blob/main/whodunit.pth)
- Accuracy increased from 91% to 94%
