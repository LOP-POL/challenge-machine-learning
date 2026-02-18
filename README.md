# Challenge coding session 2: Machine learning
## This is to Serve as a code base for our machine learing challenage coding Session
---
meanings of the column headers in the files
SZx Shot Counter
Date
Time
StZx - Piece Counter Actual Value
ZSx  - Injection Time Actual Value
APHu - Specific Pressure at Switchover
ACPx - Cushion Volume Actual Value
ZDx - Dosing Time Actual Value
ZUs - Cycle Time until End of Demolding
SFs - Mold Opening Stroke Peak Value
GEx - Total Energy Actual Value Last Cycle
GPx - Total Power Actual Value
HPx - Heating Power Actual Value
HEx - Heating Energy Actual Value Last Cycle
MPx - Motor Power Actual Value
PPx - Embossing Position Actual Value
ESPx-  Specific Total Energy Consumption


OVERALL MODEL RANKING
1. AutoML AutoGluon - our best model after final internal evaluation - F1 score with testing targets 0.93 / 1.00 but inconsistent
2. Optimized MLP - tuned a lot and good result but 0.89 when testing
3. Random Forest - needs a lot of tuning but overall best score without neural network

To use models, use model_testing_pipeline with correct model and file paths.