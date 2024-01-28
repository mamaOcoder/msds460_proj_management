\* Assignment2_bestCase_Additional *\
Minimize
OBJ: Z
Subject To
_C1: - Describe_product + Design_brochure >= 1
_C10: - Coding + Write_documentation >= 15
_C11: - Coding + Unit_testing >= 10
_C12: Package_deliverables - Write_documentation >= 3
_C13: System_testing - Unit_testing >= 8
_C14: Package_deliverables - System_testing >= 10
_C15: Develop_pricing_plan - Package_deliverables >= 2
_C16: Develop_implementation_plan - Package_deliverables >= 2
_C17: Develop_pricing_plan - Survey_potential_market >= 5
_C18: - Develop_pricing_plan + Write_client_proposal >= 2
_C19: - Develop_implementation_plan + Write_client_proposal >= 3
_C2: - Describe_product + Requirements_analysis >= 1
_C20: - Write_client_proposal + Z >= 1
_C3: - Describe_product + Develop_implementation_plan >= 1
_C4: - Develop_marketing_strategy + Survey_potential_market >= 5
_C5: - Design_brochure + Survey_potential_market >= 2
_C6: - Requirements_analysis + Software_design >= 3
_C7: - Requirements_analysis + System_design >= 3
_C8: Coding - Software_design >= 10
_C9: Coding - System_design >= 5
End
