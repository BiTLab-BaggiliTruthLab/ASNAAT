import sys, getopt
import appleParser as AP
import androidParser as AN
def main(argv):
   try:
      opts, args = getopt.getopt(argv,"ha:b:w:",['help'])  #Makes a list of arguments entered
   except getopt.GetoptError:
      print ('Usage: Tool.py [options] <inputfile>')
      sys.exit(2)

   l = len(opts)
   if l == 1 and opts[0][0] in ("-h","--help"):                #Displays help menu
      print('Usage:   Tool.py [options] <inputfile>')
      print('Example: Tool.py -a Apple.tar')
      print('Options:')
      print('         -h, --help')
      print('         -a            apple image tar')
      print('         -b            android image tar')
      sys.exit()

   elif l == 1 and opts[0][0] == "-a":                         #Apple option with default wordlist
      AP.apple(opts[0][1])
   elif l == 1 and opts[0][0] == "-b":                         #Android option with default wordlist
      AN.android(opts[0][1])
   
if __name__ == "__main__":
   main(sys.argv[1:])
