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
	AUTHOR <i>commit.author</i>
	DATE <i>commit.date</i>
	FILECOUNT <i>commit.files.filecount</i>
	
	FILENAME <i>commit.files[0].filename</i>
	ADD <i>commit.lines_added_to_file</i>
	DEL <i>commit.lines_deleted_from_file</i>
	PATCH 
	<i>patch:diff</i>

	FILENAME <i>commit.files[1].filename</i>
	ADD <i>commit.lines_added_to_file</i>
	DEL <i>commit.lines_deleted_from_file</i>
	PATCH
	<i>patch:diff</i>

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

4.  Run <b>generate_alternate.py</b>. This will generate the first 6 features:
	<pre><code>
	COMMITS, LINESADDED, LINESDEL, UNIQUEAUTHORS, COMMITFREQ60, LASTCOMMIT
	</pre></code>
    into a temporary file <b>mldata</b>

5.  Filter <b>mldata</b> to remove instances where values of all 6 features is 0. These files were not changed in between 3.1 and 3.2
	<pre><code>
	cat mldata | grep -v 0,0,0,0,0,0 > mldata_filtered
	</pre></code>
    Output to another file <b>mldata_filtered</b>

6.  
