"""
Created on 3/Jul/2022
@author: wangpengfei
@Mail: 206462763@qq.com
"""
import click

@click.command()
@click.option('-i','--input',type=click.File('r'),help='The input file',required=True)
@click.option('-w','--window',type=int,help='The input windows size',required=True)
@click.option('-z','--step',type=int,help='The input step size',required=True)
@click.option('-o','--out',type=click.File('w'),help='The output file',required=True)

def main(input,window,step,out):
            f1 = input.read()
            f1 = f1.rstrip("\n")
            f = [i.strip() for i in f1]
            l = len(f)
            left = -step
            right = window - step
            filterlist = ["TACAGT"]
            num = ((l-window)//step)+1
            for i in range(num):
                left = left + step
                right = right + step
                list1 = f[left:right]
                s=["".join(list1)]
                if filterlist[0] in s[0]:
                    out.write(str(i+1) + '\t' + str(s) + '\n')
if __name__ == '__main__':
    main()