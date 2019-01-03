import sys, os, subprocess

if len(sys.argv) < 3:
    print('Usage:\n'
          '    [python] ', sys.argv[0], ' <sourceVideo> <positionPairs>\n'
          '        <positionPairs> - Pairs of positions in format of hh:mm:ss. E.g. 00:01:00|00:02:00,00:03:00|00:04:00')
    exit(1)

vpath = sys.argv[1]
(folder, vfile) = os.path.split(vpath)
(sname, ext) = os.path.splitext(vfile)
pos_arr = str(sys.argv[2]).split(',')
if folder:
    os.chdir(folder)

cmd_ffmpeg = 'D:\\DEV\\ffmpeg-4.0.2-win64-static\\bin\\ffmpeg'
subfile_arr = []

# ===== Subfiles =====
for i in range(len(pos_arr)):
    (ss, to) = str(pos_arr[i]).split('|')
    subfile = '%s_sub%s%s' % (sname, i, ext) if len(pos_arr) == 1 else 'sub%s%s' % (i, ext)
    arg_sub = '-ss %s -to %s -i "%s" -c copy "%s" -y' % (ss, to, vfile, subfile)
    print(subfile, arg_sub)
    subfile_arr.append(subfile)

    p = os.popen('%s %s' % (cmd_ffmpeg, arg_sub))
    # print(p.read())

if len(pos_arr) > 1:
    # ===== Concatenates =====
    ofile = '%s_sub%s' % (sname, ext)
    arg_concat = '-i "concat:%s" -c copy %s -y' % ('|'.join(subfile_arr), ofile)
    p = os.popen('%s %s' % (cmd_ffmpeg, arg_concat))
    print(p.read())

    # ===== Clean subfiles =====
    for e in subfile_arr:
        os.remove(e)

os._exit(0)
sys.exit(0)
exit(0)