Social Computing Data Repository - Basic Information
==========================================================================
Dataset Name: TUAW
Abstract: TUAW is a weblog dedicated to disseminating information on Apple products and services.
Number of Instances: 10485
Number of Attributes: 11
Missing Values: yes


Source:
==========================================================================
Nitin Agarwal+, Lei Tang*, Huan Liu*, and Philip S. Yu^

+ Department of Information Science, University of Arkansas at Little Rock. E-mail:nxagarwal@ualr.edu

* School of Computing, Informatics and Decision Systems Engineering, Arizona State University. E-mail: huan.liu@asu.edu, L.Tang@asu.edu

^ Department of Computer Science, Univeristy of Illinois, Chicago. E-mail: psyu@cs.uic.edu


Data Set Information:
==========================================================================
The dataset consists of blog posts crawled from The Unofficial Apple Weblog(TUAW).TUAW is bogsite dedicated to Apple products and services. 
The blogsite consists of a closed community of bloggers, where other users are allowed to comment on the blogposts. The dataset consists of 
blogposts from the period January 2004 till February 2007, in addition to metadata like the number of inlinks.

Attribute Information:
==========================================================================
Each instance in the dataset represents a blogpost and consists of the following 11 attributes

1. Name: Title 
   Type: String.
   Info: This attribute represents the title of the blogpost.
   Missing Values: No
2. Name: Date 
   Type: String
   Info: The date the blogpost was posted on TUAW.
   Missing Values: No
3. Name: Blogger 
   Type: String
   Info: Author of the blogpost.
   Missing Values: No
4. Name: Categories 
   Type: String(Separated by :&:)
   Info: Category of the blogpost.
   Missing Values: Yes
5. Name: Post 
   Type: String
   Info: Text from the blogpost.
   Missing Values: No
6. Name: Post_Length 
   Type: int
   Info: Length of the blogpost.
   Missing Values: No
7. Name: No_of_outlinks 
   Type: int
   Info: Number of references or outlinks in the blogpost to external content.
   Missing Values: No
8. Name: No_of_inlinks 
   Type: int
   Info: Number of links citing this particular blogpost. This data was retrieved by using the link search feature of Technorati.
   Missing Values: No
9. Name: No_of_comments 
   Type: int
   Info: Number of comments received by the blogpost.
   Missing Values: No
10.Name: Comments_URL 
   Type: String
   Info: Permanent URL to the comments page.
   Missing Values: No
11.Name: Permalink 
   Type: String
   Info: Permanent link to the blogpost.
   Missing Values: No
   
Relevant Papers:
==========================================================================

