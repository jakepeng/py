import sys, os, subprocess

if len(sys.argv) < 3:
    print('Usage:\n'
          '    [python] ', sys.argv[0], ' <sourceVideo> <positionPairs>\n'
          '        <positionPairs> - Pairs of positions in format of hh:mm:ss. E.g. "000100-000200,000300-000400"')
    exit(1)

vpath = sys.argv[1]
(folder, vfile) = os.path.split(vpath)
(sname, ext) = os.path.splitext(vfile)
pos_arr = str(sys.argv[2]).split(',')
if folder:
    os.chdir(folder)

cmd_mp4box = 'D:\DEV\GPAC\MP4Box'
subfile_arr = []

# ===== Split files =====
for i in range(len(pos_arr)):
    (ss, to) = str(pos_arr[i]).split('-')
    ss = int(ss[:2]) * 3600 + int(ss[2:4]) * 60 + int(ss[4:]) +1
    to = int(to[:2]) * 3600 + int(to[2:4]) * 60 + int(to[4:]) -1
    subfile = '%s_sub%s%s' % (sname, i, ext) if len(pos_arr) == 1 else 'sub%s%s' % (i, ext)
    arg_sub = '-splitx %s:%s "%s" -out "%s"' % (ss, to, vfile, subfile)
    print(subfile, arg_sub)
	# D:\DEV\GPAC\MP4Box -splitx 1366:2105 "source.mp4" -out "source_sub0.mp4"
    subfile_arr.append(subfile)

    subprocess.run('%s %s' % (cmd_mp4box, arg_sub))

if len(pos_arr) > 1:
    # ===== Concatenates =====
    ofile = '%s_cat%s' % (sname, ext)
    arg_concat = '-flat -cat "%s" "%s"' % ('" -cat "'.join(subfile_arr), ofile)
    print(arg_concat)
	# D:\DEV\GPAC\MP4Box -flat -cat "sub0.mp4" -cat "sub1.mp4" "cat.mp4"
    
    if os.path.isfile(ofile):
        os.remove(ofile)
    subprocess.run('%s %s' % (cmd_mp4box, arg_concat))

    # ===== Clean subfiles =====
    for e in subfile_arr:
        os.remove(e)

os._exit(0)
sys.exit(0)
exit(0)