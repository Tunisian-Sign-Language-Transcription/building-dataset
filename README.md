# Building The Dataset
 In this phase, we attempt to build a dictionary for the tunisian sign language and gather datasets for our models.
  ## Context
   As a first step, we have decided to limit ourselves to the context of a medical consultation. We've worked with a general practitioner that described the medical consultation. And using that description, we've extracted a list of words that we will use for our dictionary. 
   ## Building from Scratch
   We've then sent the words to Tunisian Sign Language interpreters working with <strong>ATILS</strong> (Association Tunisienne des Interprètes en Langues des Signes) whom we've reached through the president. These interpreters sent us back the sign for each term we've picked. 
   ## Already Available Ressources
   In addition, we've used the <strong>"Medical Dictionary in Tunisian Sign Languages"</strong> which was made by <strong>AVST</strong> (Association Voix du Sourd Tunisienne) in cooperation with the French Institute. This booklet contains 160 words used in the context of a medical consultation with their respective signs. Through the help of our doctor, we've sampled 60 relevant words as a starting size for our vocabulary (we will be going back to add the rest of the words once we have a minimal viable product: a working classifier model with a certain accuracy threshold to be determined). The extracted words can be found in the <strong>words.txt</strong> file. 
   ## Automation
   We've used a python script to generate a folder for each word using Google Drive's API. We've divided the work among ourselves so that each member has 10 words. Each member shoots a video (of themselves and other people) mimicking the signs for each of their words and then uploads them to their respective folder on drive.

## Contacts
These are the various individuals and entities that helped us on this process
- Association Voix du Sourd de Tunisie.
- Association Tunisienne des Interprètes en Langues des Signes.
- Syrine Ben Othman (General practitioner awaiting thesis).