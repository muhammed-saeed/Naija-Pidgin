# SUD_Naija-NSC

# Summary

A Universal Dependencies corpus for spoken Naija (Nigerian Pidgin).

# Introduction

The corpus is based on dialogues and monologues and comprises 9,242 sentences and 140,729 tokens.

Sentences are annotated with the following metadata :
+ sent_id (which also indicates the sample file)
+ text
+ text_en (English translation)
+ text_ortho (A simplified version of text where macrosyntactic annotation has been replaced by standard punctuation)
+ speaker_id (from the NaijaSynCor Metadata)
+ sound_url (links to the corresponding sound file, AlignBegin and AlignEnd features give the miliseconds that allow for a positioning in the soundfile)

# Structure

The text has been transcribed mostly following English spelling conventions for lexical words. Grammatical words have been transcribed following consensual conventions elaborated by the annotators.

The text is segmented into illocutionary units. The end of illocutionary units is indicated by a double slash (//). The sentence nucleus containing the predicate is separated from dislocated units by "lesser than" signs (<) from left-dislocated elements, and by "greater than" signs (>) from right-dislocated units. Paradigmatic lists (coordinations, appositions, and disfluencies) are marked with curly breackets, each conjunct being separated by the pipe symbol (|). Further details can be found on the "Macrosyntactic annotation guide".

The treebank is developed in SUD (https://surfacesyntacticud.github.io/) and is converted automatically into UD.


# Deviations from UD

- We distinguish arguments and modifiers in the `obl` relation: `obl:arg`, `obl:mod`
- We use `compound:redup` for reduplications and `compound:svc` for serial verb constructions.
- We distinguish 6 types of parataxis: `parataxis:conj`, `parataxis:discourse`, `parataxis:dislocated`, `parataxis:insert`, `parataxis:obj`, `parataxis:parenth`.

Consult [the language specific documentation](http://universaldependencies.org/pcm/dep/index.html) for further details concerning subtypes.

# Acknowledgments

The treebank was created within the NaijaSynCor project, directed by Bernard Caron and funded by the ANR, the French National Research Agency.

This corpus is a pilot for the larger corpus elaborated as part of the NaijaSynCor Project (Projet-ANR-16-CE27-0007). Its main aim is to elaborate and test the annotation and procedures that are used in the ANR-project. It will be part of a larger 500kW corpus that will be projected on prosodic and information structures and analysed for sociolinguistics variation (http://naijasyncor.huma-num.fr/).

The pilot corpus was recorded in various locations in Ibadan (Nigeria) by Bukola Babalola and Opeyemi Lewis. It was transcribed, translated and tagged manually using Elan-Corpa (http://llacan.vjf.cnrs.fr/res_ELAN-CorpA_en.php) by Folakemi Ladoja, Emeka Onwuegbuzia, Biola Oyelere and Samson Tella under the supervision of Bernard Caron. It was converted to CONLL by Mourad Aouini. First annotations were done by Marine Courtin and Sandra Bellato, who developed the guidelines under the supervision of Sylvain Kahane, Bernard Caron, and Kim Gerdes.The final Universal dependencies annotations have been manually checked by Chika Kennedy Ajede, Emeka Onwuegbuzia, and Samson Tella under the supervision of Bernard Caron using the processing chain developed by Kim Gerdes and Bruno Guillaume, based on the Arborator (https://arborator.ilpga.fr) and Grew (http://grew.fr). Marine Courtin, Kim Gerdes, Bruno Guillaume, Kirian Guillier, Sylvain Kahane, Mariam Nakhlé, Yuchen Song, Emmett Strickland, Manying Zhang have helped in the correction process.

# Changelog

* 2020-11-01 v2.7
  * added 8 dialogues

* 2020-05-01 v2.6
  * added the monologues from the gold part of the NaijaSynCor corpus. 80 samples, 8k sentences, 127k tokens (90k lexical tokens and 37k punctuations).
* 2019-05-15 v2.4
  * Modifications to comply with v2.4 validation:
    * when we had to change the POS tag to comply with UD validation rules, we kept the old POS tag in XPOS, so that no information is lost
    * in case of non-projective punctuations, we attached them on the govenor of the arc that creates the non-projectivity
    * compound:redup become conj:redup
* 2018-11-15 v2.3
* 2018-04-15 v2.2
  * Initial release

The dev file is composed of the following samples:
  * `ABJ_GWA_08_David-Lifestory_MG`
  * `ABJ_INF_10_Women-Battering_MG`
  * `ABJ_NOU_02_Gimba-Lifestory_MG`
  * `ENU_34_Malaysia-Guy_MG`
  * `IBA_23_Bitter-Leaf-Soup_MG`
  * `KAD_09_Kabir-Gymnasium_MG`
  * `KAD_13_Entering-University_MG`
  * `KAD_22_Chatting-At-The-Restaurant_DG` (added in 2.7)
  * `LAG_37_Soap-Making_MG`

The test file is composed of the following samples:
  * `ABJ_GWA_14_Mary-Lifestory_MG`,
  * `IBA_15_Electrician_MG`,
  * `IBA_21_Obodo-Barracks_MG`,
  * `JOS_21_Marriage-Talk-With-Oscar-1_DG`, (added in 2.7)
  * `KAD_12_Mechanic-At-Work_MG`,
  * `KAD_17_Turkeys_MG`,
  * `LAG_21_I-Like-Stout_MG`,
  * `WAZK_07_As-E-Dey-Hot-News-Read_MG`,
  * `WAZL_08_Edewor-Lifestory_MG`,
  * `WAZL_15_MC-Abi_MG`

The train file is composed of the following samples:
  * `ABJ_GWA_02_Market-Food-Church_DG`, (added in 2.7)
  * `ABJ_GWA_03_Cost-Of-Living-In-Abuja_MG`,
  * `ABJ_GWA_06_Ugo-Lifestory_MG`,
  * `ABJ_GWA_09_Journalism_MG`,
  * `ABJ_GWA_10_Steven-Lifestory_MG`,
  * `ABJ_GWA_12_Accident_MG`,
  * `ABJ_INF_08_Impatience_DG`, (added in 2.7)
  * `ABJ_INF_12_Evictions_MG`,
  * `BEN_02_Andrew-Lifestory_MG`,
  * `BEN_08_Egusi-And-Banga-Soup_MG`,
  * `BEN_09_Tailoring-Immunization_MG`,
  * `BEN_14_BronzeFM-News_MG`,
  * `BEN_34_Tale_MG`,
  * `BEN_36_Clever-Girl_MG`,
  * `ENU_01_Salomis-Egusi-Soup-Recipe_MG`,
  * `ENU_02_Christmas-At-New-Berries_MG`,
  * `ENU_09_Angry-Neighbours_MG`,
  * `ENU_13_School-Life_DG`, (added in 2.7)
  * `ENU_17_Buying-Grocery_DG`, (added in 2.7)
  * `ENU_22_Barman-Interview_MG`,
  * `ENU_33_A-Beg_MG`,
  * `ENU_37_Dmoris-Restaurant_MG`,
  * `IBA_01_Fola-Lifestory_MG`,
  * `IBA_02_Igwe-Festival_MG`,
  * `IBA_03_Womanisers_MG`,
  * `IBA_04_Alaska-Pepe_MG`,
  * `IBA_07_Na-Love_DG`, (added in 2.7)
  * `IBA_20_Bose-Alade_MG`,
  * `IBA_31_Lens-Sermon_MG`,
  * `IBA_32_Tori-By-Samuel_MG`,
  * `IBA_33_News-Comments_MG`,
  * `IBA_34_News-Report-By-Samuel_MG`,
  * `IBA_40_Christ-Passion-Prologue_MG`,
  * `IBA_41_Christ-Passion-Finale_MG`,
  * `JOS_01_People-Of-Plateau_MG`,
  * `JOS_10_Mothers-Against-Mini-Skirts_DG`, (added in 2.7)
  * `JOS_12_How-To-Prepare-Gote-Soup_MG`,
  * `JOS_14_Chibozor-View-About-Nigeria_MG`,
  * `JOS_19_Bukuru_MG`,
  * `JOS_20_Beauty-Of-Jos_MG`,
  * `KAD_03_Why-Men-Watch-Football_MG`,
  * `KAD_10_Egusi-Soup_MG`,
  * `KAD_15_Money-Wahala_MG`,
  * `LAG_07_Johns-Biography_MG`,
  * `LAG_11_Adeniyi-Lifestory_MG`,
  * `LAG_12_Insurance_MG`,
  * `LAG_27_Shawarma_MG`,
  * `LAG_31_Road-Safety_MG`,
  * `ONI_07_Dis-Year-Na-My-Year_MG`,
  * `ONI_10_Sport-Commentary_MG`,
  * `ONI_26_News-Highlights_MG`,
  * `ONI_27_A-Hotelier-Interview_MG`,
  * `PRT_01_Banga-Soup_MG`,
  * `PRT_02_Food-And-Health_MG`,
  * `PRT_05_Ghetto-Life_MG`,
  * `PRT_07_Drummer_MG`,
  * `PRT_11_A-Man-Named-Jesus_MG`,
  * `WAZA_01_Triplea-Sports_MG`,
  * `WAZA_03_Obi-Lifestory_MG`,
  * `WAZA_05_Big-Mo_MG`,
  * `WAZA_08_Body-Matter_MG`,
  * `WAZA_09_Tv-News_MG`,
  * `WAZA_10_Bluetooth-Lifestory_MG`,
  * `WAZK_08_Fuel-Price-Increase_MG`,
  * `WAZL_02_Good-Morning-Nigeria_MG`,
  * `WAZL_03_News-On-Gmns_MG`,
  * `WAZP_03_Education_MG`,
  * `WAZP_04_Ponzi-Scheme_MG`,
  * `WAZP_07_Imonirhua-Lifestory_MG`



=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v2.2
Includes text: yes
License: CC BY-SA 4.0
Genre: spoken
Lemmas: automatic
UPOS: manual native
XPOS: not available
Features: manual native
Relations: converted from manual
Contributors: Caron, Bernard; Strickland, Emmett; Courtin, Marine; Gerdes, Kim; Guillaume, Bruno; Kahane, Sylvain; Ajede, Chika Kennedy; Onwuegbuzia, Emeka; Tella, Samson
Contributing: here source
Contact: kim@gerdes.fr
===============================================================================
