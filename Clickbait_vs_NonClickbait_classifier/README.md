Colab file link: https://colab.research.google.com/drive/1MBckX0VVFB25RXm4TpHylUFpL6oaCZNb?usp=sharing

The python file asks if user wants to enter the location of click.txt and non_click.txt, which contain the data by which the model will be trained.

Sample Input (If file is stored in some different directory say '/tmp' directory in google colab server) :
      
      Do you want to add path for click.txt? (Y/N)
      >>Y
      Enter path w/o quotes:
      >>/tmp/click.txt
      
Sample Input (If file is simply uploaded on colab which is same as file is stored in '/content' directory on google colab) :
      
      Do you want to add path for click.txt? (Y/N)
      >>N

By default the program is written by assuming that user will run program on google colab. User has to upload these data files(click.txt and non_click.txt in repository) in the 'Files' section in colab file,
which are uploaded in '/content' directory by default.

The data files are present in the repository and have been picked from public dataset available at "https://github.com/bhargaviparanjape/clickbait"
