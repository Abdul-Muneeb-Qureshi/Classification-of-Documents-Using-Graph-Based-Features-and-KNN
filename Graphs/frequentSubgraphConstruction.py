from gspan_mining.config import parser
from gspan_mining.main import main

args_str = '-s 5 -d True -l 3 -u 10 -p True -w True ../GraphDataBase/beauty_fashion_graph.txt'
FLAGS, _ = parser.parse_known_args(args=args_str.split())

gs = main(FLAGS)

