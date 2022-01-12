# kapKan

This was quite a basic forensics challenge.  You were given a word document and you were tasked to find what was suspicious about it.  I immediately broke it up into its XML components since it is a .docx file:

```
$ unzip invoice.docx
Archive:  invoice.docx
 extracting: [Content_Types].xml     
 extracting: _rels/.rels             
 extracting: word/_rels/document.xml.rels  
 extracting: word/document.xml       
 extracting: word/theme/theme1.xml   
 extracting: word/settings.xml       
 extracting: word/fontTable.xml      
 extracting: word/webSettings.xml    
 extracting: docProps/app.xml        
 extracting: docProps/core.xml       
 extracting: word/styles.xml  
```

I began to inspect these documents one-by-one to see if anything popped out as unusual.  I didn't find anything until I got to the document.xml file.  It revealed this line of XML:

```
<w:fldSimple w:instr="  QUOTE  112 111 119 101 114 115 104 101 108 108 32 45 101 
112 32 98 121 112 97 115 115 32 45 101 32 83 65 66 85 65 69 73 65 101 119 66 69 
65 68 65 65 98 103 65 51 65 70 56 65 78 65 65 49 65 69 115 65 88 119 66 78 65 68 
77 65 88 119 66 111 65 68 65 65 86 119 66 102 65 68 69 65 78 119 66 102 65 72 99 
65 77 65 66 83 65 69 115 65 78 81 66 102 65 69 48 65 78 65 65 51 65 68 77 65 102 81 65 61  ">
```

This is obviously ASCII code with some zeros missing for the numbers less than 100.  Translating this with the correct format gives you a powershell bypass:

```
powershell -ep bypass -e SABUAEIAewBEADAAbgA3AF8ANAA1AEsAXwBNADMAXwBoADAAVwBfADEANwBfAHcAMABSAEsANQBfAE0ANAA3ADMAfQA=
```

The "-e" has a strange base64 string which gives the flag when decoded:

```
H.T.B.{.D.0.n.7._.4.5.K._.M.3._.h.0.W._.1.7._.w.0.R.K.5._.M.4.7.3.}.
```

flag: ```HTB{D0n7_45K_M3_h0W_17_w0RK5_M473}```
