<h1>IR_Assignment1</h1>

<b>Course Number :</b> CS F469

<b>Contributors : </b>
<ul>
<li>G V Sandeep</li>
<li>Kushagra Agrawal</li>
<li>Snehal Wadhwani</li>
</ul>

<h3><b>Aim :</b> To implement a retrieval system based on vector space model on the given dataset</h3>

<b>Language :</b> Python v2.7.12

<h6>Working :</h6>
<ol>
<li> The entire corpus is run through a main.py file which extracts the required fields and stores it in the normalized form</li>
<li> For Eg : Date is tored in the form of an UNIX timestamp so that comparison is made easy. Outlinks, Inlinks and comments have been recalculated as 1+ log(num) where num is their value. All the words in posts and title are tokenized and stemmed according to Porter's Stemming Algorithm. The words have been stripped of spaces and case sensitivity.</li>
<li> These values are then passed to the file new_inverted.py which forms an inverted dictioanry for these individual lists</li>
<li> These dictionaries are then used by the file tfidf.py which calculates the tf idf score</li>
<li> SNEHAL PLEASE WRITE ABOUT HOW THE SCORING WORKS HERE IN THIS FORMAT PLEASE :) <li>
<li> KUSHAGRA PLEASE WRITE ABOUT HOW THE POSITIONAL INDEX WORKS HERE PLEASE IN THIS FORMAT :)</li>
<li> Tkinter GUI of pyhton is used for giving it a more professional look and making it user friendly.</li>
<li> The user has the option to narrow down his results by selecting a particular date range and category of result he wants</li>
</ol>

<h6>Setting it up:</h6>
<ol>
	<li>Extract the folder and then run GUI.py. That's it :D </li>
</ol>