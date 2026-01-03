def get_call_counts(call_logs):
    call_counts = {}
    for log in call_logs:
        if log['name'] not in call_counts:
            call_counts[log['name']] = 0
        call_counts[log['name']] += 1
    return call_counts

def get_total_call_durations(call_logs):
    total_durations = {}
    for log in call_logs:
        if log['name'] not in total_durations:
            total_durations[log['name']] = 0
        total_durations[log['name']] += log['duration']
    return total_durations

def most_frequent_caller(call_logs):
    call_counts = get_call_counts(call_logs)
    total_durations = get_total_call_durations(call_logs)
    return max(
        call_counts,
        key=lambda name: (call_counts[name], total_durations[name])
    )


def process_call_logs(call_logs, task):
    
    
        if task == 'get_call_counts':
            return get_call_counts(call_logs)
        elif task == 'get_total_call_durations':
            return get_total_call_durations(call_logs)
        elif task == 'most_frequent_caller':
            return most_frequent_caller(call_logs)
        else:
            raise ValueError("Invalid task provided.")


# #Another Method:


# def process_call_logs(call_logs, task):
#     d={}
#     for diction in call_logs:
#         d[diction["name"]]=0
        
        
        
    
#     if task == 'get_call_counts':
#         for i in call_logs:
#             d[i["name"]] = d[i["name"]]+1
            
#         return d
    
#     if task == 'get_total_call_durations':
#         for i in call_logs:
#             d[i["name"]] = d[i["name"]]+i["duration"]
            
#         return d
        
#     if task == 'most_frequent_caller':
#         temp_dict=process_call_logs(call_logs,'get_call_counts')
#         max_value = max(temp_dict.values())
#         keys_with_max_value = [key for key, value in temp_dict.items() if value == max_value]
#         if len(keys_with_max_value)==1:
#             return keys_with_max_value[0]
#         else:
#             temp_dict=process_call_logs(call_logs,'get_total_call_durations')
#             max_value = max(temp_dict.values())
#             keys_with_max_value = [key for key, value in temp_dict.items() if value == max_value]
#             if len(keys_with_max_value)==1:
#                 return keys_with_max_value[0]
#         return keys_with_max_value[0]

# Call Log Analysis
# You are provided with a call log history represented as a list of dictionaries. Each dictionary contains the following keys:

# name (str): The name of the caller.
# duration (int): The duration of the call in seconds.
# There will be multiple entries with the same name in the dataset. Implement a function process_call_logs(call_logs, task) where task is one of the following:

# get_call_counts
# Returns a dictionary with caller names as keys and the count of their calls as values.
# get_total_call_durations
# Returns a dictionary with caller names as keys and the total duration of their calls as values.
# most_frequent_caller
# Returns the name of the caller with the highest number of calls.
# If there is a tie, the name with most call duration is returned.
# Example

# call_log = [
#     {"name": "Alice", "duration": 300},
#     {"name": "Bob", "duration": 200},
#     {"name": "Alice", "duration": 100},
#     {"name": "Bob", "duration": 400},
#     {"name": "Charlie", "duration":300}
# ]
# get_call_count - {'Alice':2, 'Bob':2, 'Charlie': 1}
# get_total_call_duration - {'Alice': 400, 'Bob': 600, 'Charlie': 300}
# most_frequent_caller - 'Bob', (Alice and Bob has same number of calls but Bob has the most duration.)
    
