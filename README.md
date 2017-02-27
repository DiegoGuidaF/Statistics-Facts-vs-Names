Statistics-Facts-vs-Names
===

[![View my LinkedIn Profile at https://es.linkedin.com/in/dgfguida] (https://static.licdn.com/scds/common/u/img/webpromo/btn_liprofile_blue_80x15.png)] (https://es.linkedin.com/pub/diego-guida-f%C3%B3rneas/109/531/781)

Python project using the Panda library in order to extract the information from a psycological experiment performed on bilingual children.

The research involves two studies which investigates how ostensive cues influence knowledge acquisition in 5-year old children (Mean age: 4.9). An an object matching game was created (Involving 10 objects), in which a mix of novel (6) and familiar (4) objects had to be manipulated and placed on a board. During the game, participants were presented with incidental information, containing either facts or names associated to some of the objects, requiring a fast mapping process to retain the information. The presence of one ostensive cue was manipulated: eye contact. In the Ostensive condition, children were addressed by an actor with direct gaze towards the participant, while in the Non-Ostensive condition, the actor avoided eye contact. The retention of novel names and novel facts were checked immediately after the game, and after a one-week interval.

The experiment consisted in:  First a Training phase, in which the game was taught to the participant. On second place, an Induction phase, where information was presented in an incidental way, through a game. And afterwards, participants were tested for retention immediately, and after a one-week delay. Each session had 2 data points, one for each question being asked, which were one about a novel Fact and another about a novel Name in each Test phase.

The same Procedure was applied to Study 1 and Study 2; the only difference between them was that the facts used in Study 1 were Specific, while the ones used in Study 2 were Generic. This just supposed that the facts being presented varied, while everything else remain as in the other study


## Analysis

In order to analyse the data, the answers of the participants were coded as either correct or incorrect for all the questions. The information was entered in an Excel file and Statistical analysis was performed with Python's Panda library. Responses were coded as correct or incorrect by checking whether the object selected at test time was the object corresponding to the piece of information that the child was given about it during the Induction phase. Every participant provided responses to every word and fact test questions, resulting in 2 data points per session, with one being Name and the other one Fact.

##Results

A first T-test analysing performance over the two studies didn’t found significant differences between the two types of facts being tested (Specific and Generic facts). In consequence data from both studies was collapsed in order to better assess the effect of Condition (eye contact, no eye contact) over different types of information retainment.

A three way ANOVA over the collapsed data, with Information type (word vs. fact) and Session (session 1 vs. session 2) as within-subjects variables, and Condition (eye contact vs. no eye contact) as between-subjects variable was performed.

As expected, participants presented more correct responses when tested immediately (55.7%) compared to one week later (35.7%). The main effect of Information type was an overall better performance for facts (63.4%) than for names (28.5%). Also the eye contact Condition (51.7% vs. 40.2%) significantly increased the correct responses.
