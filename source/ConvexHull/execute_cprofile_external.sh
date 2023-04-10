../../venv/bin/python -m cProfile -o output.pstats ConvexHull.py 100
gprof2dot --colour-nodes-by-selftime -f pstats output.pstats |     dot -Tpng -o output.png
../../venv/bin/python -m snakeviz output.pstats
