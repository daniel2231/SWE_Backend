import json
from memory_profiler import memory_usage
from subprocess import Popen, PIPE
import app.result.userCode as userCode
import app.result.answerCode as answerCode

def run_efficiency_check(test_content):
    tempJson = open ("./app/result/efficiency.json", "r")
    efficiencyJson = json.load(tempJson)
    tempJson.close()

    tempJson = open("./app/result/efficiency_answer.json", "r")
    efficiency_ans = json.load(tempJson)
    tempJson.close()

    loc = efficiencyJson['overall']['loc']
    loc_ans = efficiency_ans['overall']['loc']
    diff = efficiencyJson['overall']['halstead_difficulty']
    diff_ans = efficiency_ans['overall']['halstead_difficulty']
    # 복잡도?
    cycomp = efficiencyJson['overall']['cyclomatic_complexity']
    cycomp_ans = efficiency_ans['overall']['cyclomatic_complexity']

    #Dataflow Complexity
    # This code doesn't work (Will use subprocess instead)
    # mem_usage = max(memory_usage((userCode.solution(), (test_content,)), timeout=1))
    # mem_usage_ans = max(memory_usage((userCode.solution(), (test_content,)), timeout=1))
    mem1_pid = Popen(["python", userCode.solution(*test_content)])
    mem_usage = max(memory_usage(mem1_pid))
    mem2_pid = Popen(["python", answerCode.solution(*test_content)])
    mem_usage_ans = max(memory_usage(mem2_pid))

    loc_score = loc_ans - loc
    if loc_score > 0:
        loc_final = 25 - loc_score
        if loc_final < 0:
            loc_final = 0
    else:
        loc_final = 25

    diff_score = diff_ans - diff
    if diff_score > 0:
        diff_final = 25 - diff_score
        if diff_final < 0:
            diff_final = 0
    else:
        diff_final = 25

    # dataflow complexity
    mem_usage_score = mem_usage_ans - mem_usage
    if mem_usage_ans > 0:
        mem_usage_final = 25 - mem_usage_score
        if mem_usage_final < 0:
            mem_usage_final = 0
    else:
        mem_usage_final = 25

    # cyclomatic complexity
    cycomp_score = cycomp_ans - cycomp
    if cycomp_score > 0:
        cycomp_final = 25 - cycomp_score
        if cycomp_final < 0:
            cycomp_final = 0
    else:
        cycomp_final = 25

    # make dictionary for output
    result = {
        "line_of_codes" : [loc_final, loc, loc_ans],
        "halstead_difficulty" : [diff_final, diff, diff_ans],
        "dataflow_complexity" : [mem_usage_final, mem_usage, mem_usage_ans],
        "controlflow_complexity" : [cycomp_final, cycomp, cycomp_ans]
    }

    return result

