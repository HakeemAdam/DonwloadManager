import os
import shutil

pdf_dir = r'C:\Users\mansa\Documents\dir\books'
pic_dir = r'C:\Users\mansa\OneDrive\Pictures\Saved Pictures'
vid_dir = r'C:\Users\mansa\Videos'
midi_dir = r'C:\Users\mansa\Documents\dir\Music\globalMidi'
docs_dir = r'C:\Users\mansa\Documents\dir\HfK\work_docs'
m4l_dir = r'C:\Users\mansa\Documents\dir\Music\M4L'
max_dir = r'C:\Users\mansa\Documents\dir\Work\Coding\MaxMSP'
org_dir = r'C:\Users\mansa\Downloads'


def move_file():
    for filename in os.listdir(org_dir):
        if filename.endswith(".pdf"):
            source = os.path.join(org_dir, filename)
            dest = os.path.join(pdf_dir, filename)
            dest_move = shutil.move(source, dest)
        if filename.endswith(".jpg"):
            source_pic = os.path.join(org_dir, filename)
            dest_pic = os.path.join(pic_dir, filename)
            pic_move = shutil.move(source_pic, dest_pic)
        if filename.endswith(".png"):
            source_pic = os.path.join(org_dir, filename)
            dest_pic = os.path.join(pic_dir, filename)
            pic_move = shutil.move(source_pic, dest_pic)
        if filename.endswith(".mid"):
            source_mid = os.path.join(org_dir, filename)
            dest_mid = os.path.join(midi_dir, filename)
            mid_move = shutil.move(source_mid, dest_mid)
        if filename.endswith(".docx"):
            source_doc = os.path.join(org_dir, filename)
            dest_docs = os.path.join(docs_dir, filename)
            docs_move = shutil.move(source_doc, dest_docs)
        if filename.endswith(".avi"):
            source_vid = os.path.join(org_dir, filename)
            dest_vid = os.path.join(vid_dir, filename)
            vid_move = shutil.move(source_vid, dest_vid)
        if filename.endswith(".amxd"):
            source_m4l = os.path.join(org_dir, filename)
            dest_m4l = os.path.join(m4l_dir, filename)
            m4l_move = shutil.move(source_m4l, dest_m4l)
        if filename.endswith(".maxpat"):
            source_max = os.path.join(org_dir, filename)
            dest_max = os.path.join(max_dir, filename)
            max_move = shutil.move(source_max, dest_max)


if __name__ == "__main__":
    try:
        move_file()
    except:
        pass
