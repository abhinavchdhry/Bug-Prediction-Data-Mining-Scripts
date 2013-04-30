Bug-Prediction-Data-Mining-Scripts
==================================
To gather change data between revisions 3.1 and 3.2, for instance, do:

1.  Run <b>gitdata_quick</b> with changes to <b>start_date</b> and <b>end_date</b>
    <b>start_date</b> should be release date of 3.1 and <b>end_date</b> should be release date of 3.2
    This will create a file <b>shalist</b> in the same directory which will contain commit SHAs of all commits made between the 2 dates to the repository

2.  Run <b>get_commits.py</b>. This will create .txt files for each commit in <b>shalist</b>
    The .txt files will be named in the pattern <commit_SHA.txt>
    The format of the commit files will are follows:
	<pre><code>
	AUTHOR <commit.author>
	DATE <commit.date>
	FILECOUNT <commit.files.filecount>
	
	FILENAME <commit.files[0].filename>
	ADD <commit.lines_added_to_file>
	DEL <commit.lines_deleted_from_file>
	PATCH 
	<patch:diff>

	FILENAME <commit.files[1].filename>
	ADD
	DEL
	PATCH
	<patch:diff>

	...
	...	
	...

	</code></pre>

3.  Now we need 2 files in the same folder named <b>list3_0.dat</b> and <b>list3_1.dat</b> (format: list3_x.dat)
    These will contain a list of all .java files in the org.eclipse.jdt.core sub-directory of the releases.
    They can be acquired as follows:
	Download and extract the source builds for Eclipse 3.0 and Eclipse 3.1 from archive.eclipse.org
	In the top-level directory of the 3.x release extracted folder, run:
		<pre><code>
		find -L | grep '\/org\.eclipse\.jdt\.core\/' | grep '\.java$' > list3_x.dat
		</code></pre>

