#include <string>
#include <vector>

#include "test_framework/generic_test.h"
using std::string;
using std::vector;

vector<string> Partial(const int index, const string &phone_number) {
  vector<string> mnemonics;
  static vector<string> num_to_alphabet{"0",   "1",   "ABC",  "DEF", "GHI",
                                        "JKL", "MNO", "PQRS", "TUV", "WXYZ"};
  for (auto &ch : num_to_alphabet[phone_number[index] - '0']) {
    if (index == 0) {
      mnemonics.push_back(string(1, ch));
    } else {
      for (auto &str : Partial(index - 1, phone_number)) {
        mnemonics.push_back(str + ch);
      }
    }
  }
  return mnemonics;
}

vector<string> PhoneMnemonic(const string &phone_number) {
  return Partial(phone_number.size() - 1, phone_number);
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"phone_number"};
  return GenericTestMain(args, "phone_number_mnemonic.cc",
                         "phone_number_mnemonic.tsv", &PhoneMnemonic,
                         UnorderedComparator{}, param_names);
}
