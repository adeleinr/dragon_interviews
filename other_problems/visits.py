# Background: Different providers (doctors, hospitals) charge different amounts for treatment of similar diseases depending on how efficient they are. Members also incur different costs year-round depending on how sick they are and how effective they are in finding the appropriate care. The goal of this question is to analyze these healthcare costs, and determine the highest costing members and providers that we work with.


# Assume that at the end of the year, you are given a list of members to analyze (in memory) according to the data model below.


# class Member:
#     def __init__(self, visits=None, member_id=None):
#         self.visits = visits or []
#         self.member_id = member_id

# class Visit:
#     def __init__(self, provider_id=None, diagnosis_code=None, visit_cost=0):
#         self.provider_id = provider_id
#         self.diagnosis_code = diagnosis_code
#         self.visit_cost = visit_cost


#         We need a list of the least efficient members, that together, represent threshold % of the total cost of members.

#         You will be supplied a list of Members and a threshold value

#         Write a function to return a sublist of members with the following criteria.
#         - the sum cost of the returned list is at least <threshold> % of the total input cost
#         - The returned list of members should be the smallest possible.


#         def calculate_top_x_members(members, cost_threshold_percent):
"""
           60                         90
members = [Member(visits=[10,20,30]), Member(visits=[20,30,40])]

threshold% = 20, threshold =30, => Member(visits=[20,30,40]), Member(visits=[10,20,30] or
threshold = 100 => Member(visits=[10,20,30]), Member(visits=[20,30,40])

threshold = 50 =>  Member(visits=[20,30,40])
"""


class Member:
    def __init__(self, visits=None, member_id=None):
        self.visits = visits or []
        self.member_id = member_id
        self.total_visits_cost = 0


class Visit:
    def __init__(self, provider_id=None, diagnosis_code=None, visit_cost=0):
        self.provider_id = provider_id
        self.diagnosis_code = diagnosis_code
        self.visit_cost = visit_cost


def calculate_top_x_members(members, cost_threshold_percent):
    if not members:
        return []
    total_costs = 0

    for member in members:
        curr_total_cost = 0
        for visit in member.visits:
            curr_total_cost += visit.visit_cost
        member.total_visits_cost += curr_total_cost
        total_costs += member.total_visits_cost

    members.sort(key=lambda a: a.total_visits_cost)

    threshold = (total_costs * cost_threshold_percent) / 100

    result_list = []
    for member in members:
        curr_diff = threshold - member.total_visits_cost
        if curr_diff <= 0:
            result_list.append(member)
            return result_list
