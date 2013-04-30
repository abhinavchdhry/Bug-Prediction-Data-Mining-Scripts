Bug-Prediction-Data-Mining-Scripts
==================================
To gather change data between revisions 3.1 and 3.2, for instance, do:

1.  Run <b>gitdata_quick</b> with changes to <b>start_date</b> and <b>end_date</b>
    <b>start_date</b> should be release date of 3.1 and <b>end_date</b> should be release date of 3.2
    This will create a file <b>shalist</b> in the same directory which will contain commit SHAs of all commits made between the 2 dates to the repository
    <br></br>

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
	<br></br>

3.  Now we need 2 files in the same folder named <b>list3_0.dat</b> and <b>list3_1.dat</b> (format: list3_x.dat)
    These will contain a list of all .java files in the org.eclipse.jdt.core sub-directory of the releases.
    They can be acquired as follows:
	Download and extract the source builds for Eclipse 3.0 and Eclipse 3.1 from archive.eclipse.org
	In the top-level directory of the 3.x release extracted folder, run:
		<pre><code>
		find -L | grep '\/org\.eclipse\.jdt\.core\/' | grep '\.java$' > list3_x.dat
		</code></pre>
	<br></br>

4.  Run <b>generate_alternate.py</b>. This will generate the first 6 features:
	<pre><code>
	COMMITS, LINESADDED, LINESDEL, UNIQUEAUTHORS, COMMITFREQ60, LASTCOMMIT
	</pre></code>
    into a temporary file <b>mldata</b>
    The format of <b>mldata</b>:
	<pre><code>
	FILENAME,COMMITS,LINESADDED,UNIQEAUTHORS,COMMITFREQ60,LASTCOMMIT
	</pre></code>
	<br></br>

5.  Filter <b>mldata</b> to remove instances where values of all 6 features is 0. These files were not changed in between 3.1 and 3.2
	<pre><code>
	cat mldata | grep -v 0,0,0,0,0,0 > mldata_filtered
	</pre></code>
    Output to another file <b>mldata_filtered</b>
	<br></br>

6.  Now we get the list of in-development bugs for every file. This requires a manual hack (not enough time to write a auto script)
    In <b>get_bugdata.py</b>, set <b>release_date</b> field to release date of 3.1 release
    and <b>final_date</b> field to release date of 3.2 release.
    Run <b>get_bugdata.py</b> and redirect output to a temporary file:
	<pre><code>
	python get_bugdata.py > temp
	</pre></code>
    The script looks for commits with dates between release dates of 3.1 and 3.2 but might keep running after all such commits have been found. Need to periodically check the temp file (use <code>cat</code>) to see if all such commits have been processed. If done, break the script process (Ctrl+C) and filter out SHA strings from the temp file. I used:
	<pre><code>
	cat temp | grep -E '[0-9a-z]{6,} > bug_shas.dat
	</code></pre>
	<b>bug_shas.dat</b> will now hold the SHAs of all commits to be processed for indev bug fixes.
	<br></br>

7.   Run <b>get_bug_script.py</b>. Make sure:
	```python
	f = open('bug_shas.dat', 'r')
	f1 = open('mldata_filtered', 'r')
	f2 = open('final_indev_bug_list.dat', 'w')
	```

8.   
