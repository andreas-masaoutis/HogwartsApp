# Documentation

The purpose of this document, with respect this project, is:
- to provide the vision and motivation for it 
- to record all the important choices
- to help the user navigate it.

It is a fusion of documents usually found in larger projects; ours is a tiny one but we still need some of the functionality provided by these documents.

## Vision
The goal here is to replicate the tasks performed by a data analyst, in a hypothetical job:
> As a Data Analyst, you will be responsible for delivering actionable and relevant insights, build automated dashboards, reports and advanced models to help our teams make better and faster decisions. You will work closely with the main stakeholders and help our commercial and product teams make data-driven decisions.


## Architecture
At the conceptual level, a data analysis project involves:
- to frame the problem/question and setting the objectives
- to get the data and decide on its architecture and how to persist it
- start the exploration and the clean up
- create the new features that are relevant for the questions
- built the relevant models/analysis
- communicate the findings

### Let's see how our analysis is structured.

In our case, for the problem framing we start with the questions in the description along with our understanding of the problem.

The dataset is the two csv files that contain the users and their actions. The initial data is placed on a simple flatfile "database", and all subsequent versions of the data will be stored there. The DB engine will be TinyDB - a flatfile replacement for MongoDB. The choice for a NoSQL-like solution is for the flexibility in the phase of prototyping, plus the smooth interplay between json, that is used for saving the data, and git.

A jupyter notebook is dedicated to all the necessary data engineering, from cleanup to new features. The notebook operates on the flatfile "database".

One more notebook is used for the analysis and our findings; our data story. The visualisations and other data produced here will be fed to the pdf final report.

A third notebook is the "explorative" dashboard, providing a user interface into aspects of the data.

Finally, there is pdf presentation that communicates the findings to the various stakeholders.