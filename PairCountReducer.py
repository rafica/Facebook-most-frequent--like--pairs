import sys

class PairCountReducer:
    def __init__(self):
        self.current_pair = None
        self.current_count = 0

    def run_main(self):
        for line in sys.stdin:
            try:
                if not line:continue
                pair, count = line.strip().split("\t")
                count = int(count)
                if pair == self.current_pair:
                    self.current_count += count
                else:
                    if self.current_pair:
                        print "%s\t%s" % (self.current_pair, self.current_count)
                    self.current_pair = pair
                    self.current_count = count

            except:
                continue

        if self.current_pair:
            print "%s\t%s" % (self.current_pair, self.current_count)
            
if __name__ == "__main__":
    pcr_obj = PairCountReducer()
    pcr_obj.run_main() 
