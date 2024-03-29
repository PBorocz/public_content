---
tags:
  - bayesian
  - history
  - knowledge
---

# The "Knowledge" Project Brainstorming

## Arc of Enlightenment

``` example
Data → Facts → Information → Knowledge → Insight → Wisdom
```

With thanks to Neil deGrasse Tyson (@neiltyson): [Arc of Enlightenment in a rational, civilized world](https://twitter.com/neiltyson/status/1401201102645776392?s=27)

## Introduction

The amount of "knowledge" in the world continues to expand at what seems to be an exponential pace. However, little discussion exists on the ability to understand knowledge at the "meta" level, addressing questions such as:

* How do we measure the quality of our knowledge?
* _When_ should our knowledge change over time?
* _Why_ should our knowledge change over time?
* _How_ does our knowledge change over time?
* Are their prescriptive notions of how knowledge _should_ change over time?
* How do the answers to these questions vary across disciplines?
* How/where should knowledge be kept? aka Library of Alexandria vs. S3?

{==I propose that what's missing is a formal mathematical *model* of knowledge itself.==}

By way of analogy, one of the fundamental breakthroughs in computer science in the late 70's was a conceptual and mathematical model of "data storage" design (i.e. the Relational Data Model \[ref Codd/Date\]). This model is not a model of any particular data to be stored (e.g. accounting ledgers, health records, CERN results) but a "_meta_" model of how to represent structured data in a way that minimized the duplication of data (and thus the operations needed to maintain it) with a rigorous mathematically consistent underpinning. Over a half-century later, the relational model is still the core meta-design model for the overwhelming amount of data held today.

However, the relational data meta model only represents data. We distinguish information from data through *either* the following two precepts:

* Information is data (or a derivative of data) that can or does influence an actual, real-world decision (not necessarily human) This is based on the long-standing influence of learning Decision Analysis at Stanford in the mid-80's.

* Information is that which affects "knowledge".

The core cycle here can be inferred as:

**Data** :material-arrow-right: (analysis) :material-arrow-right: **Information** :material-arrow-right: (weighting) :material-arrow-right: **Knowledge** :material-arrow-right: (decision-making) :material-arrow-right: **Decisions** :material-arrow-right: (outcomes) :material-arrow-right: **Data** (...rinse & repeat)

As we'll see below, the weighting process step here is critical...based on new information, how to we update collective knowledge in the respective domain?

## Examples

### Nutrition

Given a the release of new research paper on Nutrition, do we or don't we change any of the following:

   * Our own diets?
   * Recommendations to physicians obo their patients?
   * School or other institutional diets?
   * Government diet recommendations?

### SARS-COV2 

Given the torrent of research performed and published during the SARS-COV2 pandemic:

   * How and when do we change our own or our family's behaviour based on the release of any new research?
   * What _existing_ policies should change?
   * What _new_ policies at the local, state and federal level should be enacted?


## Evaluating The Quality of Research

For each and every paper we run across, we must _scientifically_ evaluate it's quality (as the higher the quality of research, the more strongly both or own and the collective knowledge of society should be updated). To determine this strength, we ask a reasonably standard list of scientific literacy questions, of which only a small sample are:

* Was the hypothesis properly formulated? [^1]
* How broad was the sample set?
* What is single blind? double blind?
* Were high-quality statistics used?
* Could there be a *control* group? If so, was there?
* etc.

## Core Precepts

### Information is That Which Updates Existing Knowledge

Information from research (as opposed to _data_) can have qualities that directly determine the ability to update knowledge. For example:

* Information that comes from sources that have exhibited a strong history of knowledge updates probably should have a higher impact on future knowledge updates.

* Information that is independently corroborated has a higher impact on knowledge updates.

* Information that comes from less-biased sources has a higher impact on knowledge updates.

* Information that comes from scientifically rigorous processes has a higher impact on knowledge updates.

### Knowledge is Inherently Probabilistic

We used to *know* that the earth was flat (and that it was the center of our solar system). Essentially, everything we think we know is simply a probabilistic estimation of it's certainty (a bit like quantum mechanics can't give us the absolute location of an electron, only a probabilistic wave). Thus, as new information arises, the probabilities associated with what we know can change. At first, this seems rather impractical and without structure (ie. do we jump at every single paper that comes out trying to prove some "wacky" new hypothesis?).

However, we actually *do* have a formal meta-model for this -> LaPlace and Bayes. Bayes' Theorem provides a reasonably rigorous meta-model for how current probability estimates should change based on new information  [^2].

### Knowledge *Distribution* is an Active Process.

Information leading to knowledge updates can start in well-known arenas, ranging from well-known and established journals through ad-hoc research from iconoclastic individuals.

As an example, the knowledge distribution process for general "hard-science" topics can be roughly described by the following:

1. Individual research projects beget papers.
- Papers that meet some level of quality and/or approval are formally published in journals (albeit they might have been already distributed to PLOS/Arxiv environments).
- Publishing of interesting/controversial/new information begets more research and more papers, particularly at a broader swathe of post-graduate programs and levels.
- The increase in corroborative papers begets formal discussion at the graduate education level.
- This discussion begets codification and incorporation of these ideas in upper-level undergraduate curricula and discussions.
- This curricula slowly filters down over time to lower-level undergraduate textbooks and discussion.
- College textbook representations beget more simplified representations in high school textbooks.
- If appropriate, knowledge from high school textbooks trickles down to junior high and middle/elementary school textbooks (at which point we'd probably consider this "common" knowledge from a societal perspective).

Based on the complexity of the respective knowledge, not all of these steps are appropriate; for example, we don't expect to teach the basics of polymerase chain reaction in middle-school \[at least not yet\]). In contrast, while it took decades, discussion of black holes is clearly seen as an appropriate part of high-school astronomy classes. As to how /long/ this trickle down takes, an interesting case study will be to see how long it takes for the most current change in the debate regarding the warm-blooded vs. cold-blooded nature of dinosaurs to trickle down to elementary school textbooks.

Whether or not knowledge *does* trickle down is a question in and of itself (and will be discussed below). At each step in a diffusion process such as this, knowledge could "stop" (for various reasons, also discussed below).

Finally, every "field" has it's own unique twists and peculiarities over their specific knowledge distribution (levels of openness, different levels of "certainty" to be achieved before publishing, different biases from funding etc.). High-energy particle physics seems to have *very* high bars before definitive conclusions are promulgated. Conversely, issues with small sample sizes, lack of control groups, difficulty in controlling for exogenous factors make even the strongest pronouncements from nutrition researchers questionable [^3]. 

### Knowledge Has a Half-Life

Knowledge decays over time, irrespective of how or even if, it's actually used. For example:

* Knowledge can become embedded into systems ("essentially" disappearing).

* Knowledge can simply get forgotten based on the medium in/on which it's stored and our prevalence for using easier-to-use systems (google & wikipedia vs. a physical library a la Alexandria).

* Older knowledge doesn't carry it's own meta data, describing how it was formulated (what basis, what research, etc.) This inherently creates a bias against older knowledge in favour of that which has been created more recently.

## Building Blocks of Mental Models

With this context, we can finally posit that the following models to form the intellectual basis of a knowledge management meta-model, each of which brings a core set of behavior to the various factors above:

* For knowledge *updates*, **[Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem)** is perfectly suited. Existing knowledge is treated as our "prior" distribution while new information (with the appropriate weighting) is used to update this prior to come up with a new posterior, i.e. our current/best state of knowledge.

* For knowledge *distribution*, **[Diffusion](https://en.wikipedia.org/wiki/Diffusion_of_innovations)** or percolation models are an effective way of modeling distributions across various networks.

* Finally, for knowledge *decay*, **[Half-life](https://en.wikipedia.org/wiki/Half-life)** or decay models are an effective way of modeling the degree to which something disappears.

Some of these models are used in a descriptive fashion (e.g. diffusion) while I mean some on more of a prescriptive basis (e.g. the recommendation to manage the quality of knowledge on a probabilistic basis).

---

### Examples of "Knowledge-Changing" Research in Every Day Articles

* [Diamond samples in Canada reveal size of lost continent](https://www.bbc.com/news/world-us-canada-51989255) : Canadian scientists have discovered a fragment of an ancient continent, suggesting that it was 10% larger than previously thought.

* [A long-standing and fundamental question about dinosaurs may finally have an answer](https://www.cnn.com/2022/05/25/world/dinosaur-blood-warm-cold-scn/index.html "Where Dinosaurs Warm or Cold-Blooded?") : Fearsome predators like T. rex and towering, telescope-necked dinosaurs, such as Brachiosaurus, were warm-blooded creatures in the same way birds and mammals are, according to a groundbreaking new study.

* [Why the Coronavirus Is So Confusing](https://www.theatlantic.com/health/archive/2020/04/pandemic-confusing-uncertainty/610819) (good article on the need for (and importance of) probabilistic knowledge (indirectly).

## Background Links on Mental Models

* [Methods and visualization tools for the analysis of medical, political and scientific concepts in Genealogies of Knowledge](https://www.nature.com/articles/s41599-020-0423-6) (Nature, 2020-03-20)
* [The Lindy Effect](https://en.wikipedia.org/wiki/Lindy_effect) (essentially that the longer something has stayed around, the longer it *will* stay around).

* [One Process \| Reaction Wheel](http://reactionwheel.net/2020/04/one-process.html)

* [Metaculus: Pandemics](https://pandemic.metaculus.com/questions/) a crowd-sourced probabilistic forecasting environment.

## Probabilistic Modeling

### Background

Mostly a list of articles and packages for potential implementation should I ever decide to write any code to try and demonstrate these models.

* [A careful walk through probability distributions, using Python (PyCon 2020)](https://us.pycon.org/2020/schedule/presentation/122/) "_In this talk, we will do more than just a random walk through probability. In particular, by using Python code as an anchor, we will explore what a probability distribution as an "object" is, especially in a modeling context. By the end of this talk, probability distributions, sampling (or generating data) from a probability distribution, and the basic terms of joint, conditional and marginal distributions, should be demystified for you, and you should leave with a solid working knowledge of probability to go further and deeper with Bayesian statistics beyond PyCon!_"

* [Monte Carlo Simulation Engine In Python](https://medium.com/fintechexplained/monte-carlo-simulation-engine-in-python-a1fa5043c613) (with options trading!)

* [Monte Carlo simulation in Python \| Bartosz Mikulski](https://www.mikulskibartosz.name/monte-carlo-simulation-in-python/)

* [Monte Carlo Simulations with Python (Part 1) - Towards Data Science](https://towardsdatascience.com/monte-carlo-simulations-with-python-part-1-f5627b7d60b0)

* [Monte Carlo Simulation with Python - Practical Business Python](https://pbpython.com/monte-carlo.html) - [Initial Version](https://github.com/chris1610/pbpython/blob/master/notebooks/Monte_Carlo_Simulation.ipynb), [Optimised Version](https://github.com/chris1610/pbpython/blob/master/notebooks/Monte_Carlo_Simulationv2.ipynb)
   
* [A Math Equation Can Help Keep You Safe from COVID-19](http://nautil.us/blog/let-game-theory-tell-you-when-its-time-to-go-shopping?utm_source=pocket&utm_medium=email&utm_campaign=pockethits) (fun example problem to solve probabilistically)

### Relevant Packages

* [PyMC3 Documentation --- PyMC3 3.8 documentation](https://docs.pymc.io/)

---

[^1]: My favorite example of this is pharmaceutical research where the "control" for testing the efficacy of a potential drug is a **placebo**, *not* the best current drug treatment.

[^2]: From this, you can clearly see I fall into the "Bayesian" school of statistical thought instead of the "Frequentist" one :wink:.

[^3]: These example are *not* meant to either disparage nutrition researchers or put particle physics researchers on a pedestal; institutional, logistical and physical constraints present clear limits to high-quality research across every discipline. What we /can/ do though is formally incorporate these constraints into the process by which we update our knowledge.
