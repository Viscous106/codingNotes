# BSDA2001 — Introduction to DL and GenAI
## Week-by-week study plan

**Course:** BSDA2001, 4 credits, 12 weeks · IITM BS Data Science
**Instructors:** Prof. Balaji Srinivasan, Prof. Ganapathy Krishnamurthi
**Framework:** TensorFlow / Keras · **Co-requisite:** BSCS2008
**Course page:** https://study.iitm.ac.in/ds/course_pages/BSDA2001.html
**Official lectures:** https://www.youtube.com/playlist?list=PLZ2ps__7DhBa9hqi20allqocTSUUt3nWX

---

## Two things to know before starting

**Your course is Keras, not PyTorch.** Weeks 2, 4, 6 and 9 are hands-on in
TensorFlow/Keras. PyTorch material is tagged `[PyTorch]` below so you know when
you're switching frameworks — useful for BSDA2001P (the project course), not for
these labs.

**Stanford CS230's playlist is not a curriculum.** It's a flipped classroom: the
teaching lives in Coursera modules assigned as homework, and the ten YouTube
lectures are seminars. Four are worth your time and are slotted into the weeks
they belong to. Full audit at the bottom.

**Tags:** `[Primary]` graded source · `[Core]` main teaching · `[2nd]` reinforcement
`[Keras]` · `[PyTorch]` · `[Theory]` no code

---

# PART I — Neural networks (weeks 1–2)

## Week 1 — Artificial Neural Networks (Theory)
*Syllabus: artificial neurons, layers, activation functions, loss metrics.*

- [ ] **Official course lectures — Week 1** `[Primary] [Theory]`
  https://www.youtube.com/playlist?list=PLZ2ps__7DhBa9hqi20allqocTSUUt3nWX
  Watch first. Exam questions come from here, in this notation.

- [ ] **3Blue1Brown ch.1 — "But what is a neural network?"** `[2nd] [Theory]`
  https://www.youtube.com/watch?v=aircAruvnKk
  The best 19 minutes on why a neuron is a weighted sum plus an activation.
  Then run chapters 2–4 (gradient descent, backprop, backprop calculus) from
  the series index: https://www.3blue1brown.com/

- [ ] **CampusX "100 Days of Deep Learning" — perceptron → loss functions** `[Core] [Keras]`
  https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn
  Your workhorse for weeks 1–6. Perceptron, MLPs, forward prop, backprop, in Keras.

- [ ] **MIT 6.S191 Lecture 1 — Intro to Deep Learning** `[2nd] [Theory]`
  https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI
  One hour, fast, frames the whole field.

## Week 2 — Building networks in Keras (Practice)
*Syllabus: hands-on TensorFlow/Keras; experimenting with activations and optimizers.*

- [ ] **Official course lectures — Week 2** `[Primary] [Keras]`
  Do the notebooks alongside, not after.

- [ ] **CampusX — optimizers, batch norm, dropout, vanishing gradients** `[Core] [Keras]`
  https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn
  This stretch is where "experiment with activations and optimization methods"
  actually gets taught.

- [ ] **Deep Learning Specialization C1 & C2 (Andrew Ng)** `[2nd] [Keras]`
  https://www.coursera.org/specializations/deep-learning
  Optional but strong. Note: the specialization page says it is NOT free to
  audit — financial aid is the route.

---

# PART II — Vision (weeks 3–4)

## Week 3 — Convolutional Neural Networks (Theory)
*Syllabus: CNN architecture basics, convolution and pooling layers.*

- [ ] **Official course lectures — Week 3** `[Primary] [Theory]`

- [ ] **CampusX — CNN block** `[Core] [Keras]`
  https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn
  Padding and strides, pooling, CNN vs ANN, backprop in CNNs, LeNet-5.
  Covers week 3 almost line for line.

- [ ] **MIT 6.S191 Lecture 3 — Deep Computer Vision** `[2nd] [Theory]`
  https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI
  Clearest single-sitting account of why convolution is the right prior for images.

## Week 4 — Image classification (Practice)
*Syllabus: MNIST and CIFAR-10 in Keras.*

- [ ] **Official course lectures — Week 4** `[Primary] [Keras]`

- [ ] **CampusX — cat vs dog project, transfer learning, fine-tuning vs feature extraction** `[Core] [Keras]`
  https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn
  Transfer learning isn't named in your syllabus but it's how every real image
  task gets done — and it makes CIFAR-10 far less frustrating.

---

# PART III — Sequences (weeks 5–6)

## Week 5 — RNNs and LSTMs (Theory)
*Syllabus: recurrent architectures for sequential data.*

- [ ] **Official course lectures — Week 5** `[Primary] [Theory]`

- [ ] **CampusX — RNN and LSTM block** `[Core] [Keras]`
  https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn
  Why RNNs, RNN vs ANN, types of RNN, backprop through time, LSTM architecture,
  GRU, stacked and bidirectional variants.

- [ ] **StatQuest — Long Short-Term Memory, Clearly Explained** `[2nd] [Theory]`
  https://www.classcentral.com/course/youtube-long-short-term-memory-lstm-clearly-explained-133817
  If the three LSTM gates don't click anywhere else, they will here. 21 min.

- [ ] **MIT 6.S191 Lecture 2 — Deep Sequence Modeling** `[2nd] [Theory]`
  https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI

## Week 6 — Sentiment, text generation, time series (Practice)

- [ ] **Official course lectures — Week 6** `[Primary] [Keras]`

- [ ] **CampusX — sentiment analysis with Keras, next-word prediction, stacked LSTM** `[Core] [Keras]`
  https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn
  Two of your three tasks, with code. Time series adapts from the same pattern.

- [ ] **MIT 6.S191 Lab — music generation with RNNs** `[2nd] [Keras]`
  https://introtodeeplearning.com/
  A Colab notebook, genuinely fun, same mechanics as text generation.

---

# PART IV — Generative models (weeks 7–9)

## Week 7 — Autoencoders, VAEs, GANs (Theory)

- [ ] **Official course lectures — Week 7** `[Primary] [Theory]`

- [ ] **MIT 6.S191 Lecture 4 — Deep Generative Modeling** `[Core] [Theory]`
  https://www.youtube.com/watch?v=R8V8CbuxryI
  Autoencoder → VAE → GAN in one lecture, in that order. Best single resource
  for week 7.

- [ ] **Stanford CS230 Lecture 4 — Adversarial Robustness and Generative Models** `[2nd] [Theory]`
  https://www.youtube.com/watch?v=aWlRtOlacYM
  One of four CS230 lectures worth watching. Weighted toward adversarial
  examples with GANs after — context, not your GAN lecture.

## Week 8 — Diffusion models (Theory)
*Syllabus: diffusion probabilistic models, training and inference.*

> **Thinnest week for free material.** No major free course has a proper
> diffusion lecture — MIT touches it inside generative modeling, CS230 skips it
> entirely. Lean harder on the official lectures here than anywhere else.

- [ ] **Official course lectures — Week 8** `[Primary] [Theory]`
  Prof. Krishnamurthi's research area. Expect it taught well and examined closely.

- [ ] **Outlier — Diffusion Models, Paper Explanation / Math Explained** `[Core] [Theory]`
  https://www.classcentral.com/course/youtube-diffusion-models-paper-explanation-math-explained-133593
  33 min: forward and reverse process, architecture, DDPM loss derivation.
  Best free explanation of the actual maths.

- [ ] **Outlier — How diffusion models work, explanation and code** `[2nd] [PyTorch]`
  https://www.youtube.com/watch?v=I1sPXkm2NH4
  Implementation companion to the above. Watch second.

- [ ] **Hugging Face Diffusion Models Course — Unit 1** `[Core] [PyTorch]`
  https://github.com/huggingface/diffusion-models-class
  Theory plus a notebook training a small diffusion model from scratch.
  Free; needs a HF account to push models.

## Week 9 — Generating images (Practice)

- [ ] **Official course lectures — Week 9** `[Primary] [Keras]`

- [ ] **HF Diffusion Models Course — Units 2 & 3** `[Core] [PyTorch]`
  https://github.com/huggingface/diffusion-models-class
  Fine-tuning and guidance, then Stable Diffusion. Exactly "pretrained diffusion
  models for image generation", with working notebooks.

- [ ] **CampusX — GAN implementation** `[2nd] [Keras]`
  https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn
  Keep one GAN implementation in Keras so you aren't switching frameworks for
  the graded lab.

---

# PART V — Language models (weeks 10–12)

## Week 10 — Transformers and attention (Theory)
*Syllabus: word embeddings, tokenization, attention mechanisms.*

- [ ] **Official course lectures — Week 10** `[Primary] [Theory]`

- [ ] **3Blue1Brown ch.5 (Transformers) and ch.6 (Attention, step-by-step)** `[Core] [Theory]`
  https://www.3blue1brown.com/lessons/gpt/
  ~27 and ~26 minutes. Ch.5 gives embeddings and overall shape; ch.6 is the
  clearest visual account anywhere of query, key and value.

- [ ] **Karpathy — Let's build GPT: from scratch, in code, spelled out** `[Core] [PyTorch]`
  https://www.youtube.com/watch?v=kCc8FmEb1nY
  ~2 hours: bigram baseline, attention as message-passing, multi-head, MLP,
  residuals, layernorm. Worth it despite PyTorch — the architecture is the point.
  Part of Zero to Hero: https://karpathy.ai/zero-to-hero.html

## Week 11 — BERT, decoders and fine-tuning (Theory)
*Syllabus: BERT, decoders, machine translation, LoRA, PEFT.*

- [ ] **Official course lectures — Week 11** `[Primary] [Theory]`

- [ ] **Hugging Face LLM Course — LoRA (Low-Rank Adaptation)** `[Core] [PyTorch]`
  https://huggingface.co/learn/llm-course/chapter11/4
  Why training small matrices on attention weights cuts trainable parameters
  ~90%. Earlier chapters cover tokenizers and BERT-style fine-tuning.

- [ ] **Hugging Face smol course — LoRA and PEFT** `[2nd] [PyTorch]`
  https://huggingface.co/learn/smol-course/unit1/3a
  Shorter, more practical: configuring LoRA, loading and merging adapters.

## Week 12 — Prompting (Practice)

- [ ] **Official course lectures — Week 12** `[Primary] [Theory]`

- [ ] **Stanford CS230 Lecture 8 — Agents, Prompts, and RAG** `[Core] [Theory]`
  https://www.youtube.com/watch?v=k1njvbBmfsw
  The one CS230 lecture that lands squarely on a week of your syllabus.

- [ ] **HF LLM Course — prompting and SFT chapters** `[2nd] [PyTorch]`
  https://huggingface.co/learn/llm-course/chapter11/4
  Prompt fine-tuning sits next to supervised fine-tuning; read both to see
  where the line is.

---

# Appendix A — What CS230 actually covers

All ten Autumn 2025 lectures against your twelve weeks. CS230's teaching content
is the Coursera modules assigned as homework, which is why there is no ANN, CNN,
RNN or transformer lecture in the playlist.

Playlist: https://www.youtube.com/playlist?list=PLoROMvodv4rNRRGdS0rBbXOUGA0wjdh1X
Syllabus: https://cs230.stanford.edu/syllabus/

| # | Title | Your week |
|---|-------|-----------|
| 1 | [Introduction to Deep Learning](https://www.youtube.com/watch?v=_NLHFoVNlbg) | Logistics and motivation only |
| 2 | [Supervised, Self- & Weakly Supervised Learning](https://www.youtube.com/watch?v=DNCn1BpCAUY) | — |
| 3 | [Full Cycle of a DL Project](https://www.youtube.com/watch?v=MGqQuQEUXhk) | Off-syllabus, worth watching |
| 4 | [Adversarial Robustness and Generative Models](https://www.youtube.com/watch?v=aWlRtOlacYM) | Week 7, partly |
| 5 | Deep Reinforcement Learning | — |
| 6 | [AI Project Strategy](https://www.youtube.com/watch?v=s6JVGzABKho) | Off-syllabus, worth watching |
| 7 | No class | — |
| 8 | [Agents, Prompts, and RAG](https://www.youtube.com/watch?v=k1njvbBmfsw) | **Week 12** |
| 9 | [Career Advice in AI](https://www.youtube.com/watch?v=AuZoDsNmG_s) | — |
| 10 | [What's Going On Inside My Model?](https://www.youtube.com/watch?v=Ozb1AR_F5MU) | Off-syllabus, worth watching |

---

# Appendix B — Two more things worth checking

- **Your own professors teach an NPTEL course.**
  [Machine Learning for Engineering and Science Applications](https://nptel.ac.in/courses/106106198)
  is by Balaji Srinivasan and Ganapathy Krishnamurthi — the same two names on
  BSDA2001. Same notation and emphasis usually beats a better-produced foreign
  course. The syllabus page wouldn't load for me, so check the week list before
  committing.

- **Mitesh Khapra's NPTEL Deep Learning** (IIT Madras) is the rigorous Indian
  option if you want the maths done properly rather than visually.

---

# Notes on the links

**Syllabus source:** the twelve weeks, framework, instructors and official
playlist all come from the BSDA2001 course page. The CS230 structure comes from
its published syllabus and the Autumn 2025 playlist.

**Where links point:** CampusX and MIT entries link to the playlist or course
site rather than a numbered lecture, because lecture numbering shifts between
editions — find the named topic in the list. Two entries link to Class Central
rather than YouTube, because that was the canonical page I could confirm.
