# Assignment 2: Network Models- Project Management

## Problem Setup
Our group has met multiple times to discuss this project and to work through it together as a team. We all collaborated to tackle the excel spreadsheet and to decide the workforce power necessary to complete each individual task. Given the diverse components of the project timeline, we encountered some uncertainty. While attempting to find general timelines for these tasks through Google searches and our knowledge, we often faced challenges due to the broad estimates our research would yield. Regarding cost estimates, we opted for a uniform rate. Determining distinct rates for each employee proved challenging, particularly because we were not familiar with prevailing market prices for specific roles, leading our research to provide various rates. Consequently, we settled on a fair market rate of $35 per hour for these jobs.

## Project Overview
We are thrilled to present our proposal for the development of a cutting-edge consumer recommendation system, designed to highlight and celebrate the diverse and vibrant restaurant scene in Marlborough, Massachusetts. Leveraging the insightful and rich data drawn from Yelp reviews, our system is poised to offer highly personalized and dynamic restaurant recommendations. This tailored approach aims not only to enrich the dining experiences of our users but also to bolster local businesses by connecting them with a broader audience.


In this report, we will outline three distinct scenarios that detail the development timelines for the recommendation system. Each scenario is carefully crafted to balance project efficiency with thoroughness, ensuring that we meet a range of potential needs and constraints.
## [Development Formulation](https://github.com/mamaOcoder/msds460_proj_management/blob/main/Assignment%202/Project%20Plan%20-%20Sheet1.csv)
We have meticulously outlined the various stages required for the successful development and delivery of our software. For each of these stages, we have conducted detailed estimations of the required hours and the necessary staffing resources. To provide a realistic and comprehensive timeline, our approach includes three distinct projections: the worst-case, expected-case, and best-case scenarios.

This multi-scenario planning ensures that our estimates are not only pragmatic but also adaptable to various contingencies and developments. By considering a range of possibilities, from the most ideal to the most challenging, we aim to avoid any overestimation of the completion time and ensure a smooth and efficient project flow.

Here is a directed graph where each node represents a stage, and the numbers on the edges between nodes indicate the time required in the best, expected, and worst-case scenarios, respectively.

![directed_graph](https://github.com/mamaOcoder/msds460_proj_management/blob/main/Assignment%202/directed%20graph.png)

## [Linear Programming (Python Code)](https://github.com/mamaOcoder/msds460_proj_management/blob/main/Assignment2.py) 
We have solved the linear programming problem under three different scenarios, accompanied by Gantt charts to facilitate a clearer understanding of the time required in each case: 

- [Best Case](https://github.com/mamaOcoder/msds460_proj_management/blob/main/Assignment%202/best_case_solution.txt): 53 hours

![Best_Case_Gnart](https://github.com/mamaOcoder/msds460_proj_management/blob/main/Assignment%202/best_case_gnart.png)

- [Expected Case](https://github.com/mamaOcoder/msds460_proj_management/blob/main/Assignment%202/expected_case_solution.txt): 70 hours
  
![Expected_Case_Gnart](https://github.com/mamaOcoder/msds460_proj_management/blob/main/Assignment%202/expected_case_gnart.png)

- [Worst Case](https://github.com/mamaOcoder/msds460_proj_management/blob/main/Assignment%202/worst_case_solution.txt): 95 hours

![Worst_Case](https://github.com/mamaOcoder/msds460_proj_management/blob/main/Assignment%202/worst_case_gnart.png)

## Pricing 
We are flexible in negotiating the pricing structure for our product. Our primary consideration is to ensure profitability, with the assumption that our sole capital expense is the labor cost, fixed at $35 per hour for all team members involved in the project. However, it's important to note that the final price may be subject to adjustment to account for additional capital expenditures, including operational costs and other overheads.

## Additional Contractor Impacts 
Drawing from the insights of the [sensitivity report](https://github.com/mamaOcoder/msds460_proj_management/blob/main/Assignment%202/sen_report.txt), we pinpoint Constraint _C11 (Coding + Unit_testing) as a pivotal juncture where the engagement of a specialized contractor could safeguard against any dip in activity that might precipitate an uptick in the objective value. By deploying a specialist with targeted expertise to diligently oversee and maintain the pace of the tasks encapsulated by this constraint, we can significantly bolster our adherence to the projected schedule.

Similarly, for constraints such as _C12 (Package_deliverables - Write_documentation) and _C17 (Develop_pricing_plan - Survey_potential_market), which have been earmarked as critical, the strategic allocation of additional skilled personnel to accelerate progress is anticipated to serve as a bulwark against time overruns. This proactive measure will not only curtail the likelihood of delay-induced extensions in the project timeline but also enhance the overall robustness of our timeline commitments.

By bringing an additional contractor on board to expedite the coding phase (D4) of the project, we can potentially reduce the workload by 5 hours. This strategic augmentation of our team could lead to an earlier delivery time, potentially trimming the timeline to as little as [48 hours](https://github.com/mamaOcoder/msds460_proj_management/blob/main/Assignment%202/Additional_Contract_on_Best_Case.txt).
