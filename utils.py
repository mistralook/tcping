import argparse


def statistics(time_list: list, *args):
    time_list = time_list or [0, 0, 0]
    mx = max(time_list)
    mn = min(time_list)
    avg = sum(time_list) / len(time_list)
    print(f'''
Ping statistics for {args[0]}:{args[1]}
    {args[2]} probes sent
    {args[3]} successful, {args[4]} failed
Approximate trip times in milli-seconds:
    Minimum = {mx:0.3f}ms, Maximum = {mn:0.3f}ms, Average = {avg:0.3f}ms
       ''')


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain')
    parser.add_argument('-c', '--count')
    parser.add_argument('-t', '--timeout')
    return parser
