import socket
import sys
from timer import Timer
from utils import statistics, create_parser


def ping(host, port, timeout, count=5):
    sends_count = 0
    pos_sends = 0
    neg_sends = 0
    time_list = list()
    timer = Timer()
    for _ in range(count):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,
                          socket.IPPROTO_TCP)
        s.settimeout(timeout)
        timer.start()
        try:
            s.connect((host, int(port)))
            s.shutdown(socket.SHUT_RD)
        except (socket.timeout, ConnectionRefusedError):
            print('Seems that port is unavailable or there was a timeout')
        elapsed_time = timer.stop()

        if elapsed_time < timeout:
            print(f'Probing {host}:{port}/tcp - Port is Open'
                  f' - time={elapsed_time:0.3f}ms')
            time_list.append(elapsed_time)
            pos_sends += 1
        else:
            neg_sends += 1
        sends_count += 1

    statistics(time_list, host,
               port, sends_count,
               pos_sends, neg_sends)


def main():
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    domain = args.domain.split(':')[0]
    port = args.domain.split(':')[1] \
        if len(args.domain.split(':')) == 2 else 80
    timeout_ms = float(args.timeout)
    count = int(args.count)
    host = socket.gethostbyname(f'{domain}')

    ping(host, port, timeout_ms, count)


if __name__ == "__main__":
    main()
