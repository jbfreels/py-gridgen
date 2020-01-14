import getopt
import sys

import matplotlib.pyplot as plt

uOpts = "ho:x:y:"
gOpts = ["help", "output=",
         "xaxis=", "yaxis=",
         "xlabel=", "ylabel=",
         "title="]


def usage():
    print("usage: {}".format(sys.argv[0]))
    print("  -o, --output\tfile\toutput filename, if not sepcified, output will show on screen")
    print("  -x, --xaxis\tmin,max\tmin and max for x-axis")
    print("  -y, --yaxis\tmin,max\tmin and max for y-axis")
    print("  --xlabel\tlabel\tset the label for the x-axis")
    print("  --ylabel\tlabel\tset the label for the y-axis")
    print("  --title\ttitle\tadd a centered title to the grid")


if __name__ == "__main__":
    output = None
    xlabel = None
    ylabel = None
    title = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], uOpts, gOpts)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        elif o in ("-x", "--xaxis"):
            xaxis = a.split(',')
        elif o in ("-y", "--yaxis"):
            yaxis = a.split(',')
        elif o in ("--xlabel"):
            xlabel = a
        elif o in ("--ylabel"):
            ylabel = a
        elif o in ("--title"):
            title = a

    plt.axis([int(xaxis[0]), int(xaxis[1]), int(yaxis[0]), int(yaxis[1])])
    plt.grid(b=True, linestyle='-')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.suptitle(title)

    if not output:
        plt.show()
    else:
        plt.savefig(output)
