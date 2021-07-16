h,w,n = list(map(int,input().split()))
# print(h,w,n)
# 3 3 3

acml_sum = 0
acml_sums = []
for _ in range(h):
    nums = list(map(int,input().split()))
    temp = []
    for num in nums:
        acml_sum += num
        temp.append(acml_sum)
    acml_sums.append(temp)
# [[1, 3, 6], [10, 15, 21], [28, 36, 45]]

for _ in range(n):
    x,y = list(map(int,input().split()))

# 解答
#include <iostream>

using namespace std;

int main() {
  int H, W, N;
  cin >> H >> W >> N;
  int A[H][W], sum[H][W];

  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      cin >> A[i][j];
      sum[i][j] = A[i][j];
      if (0 < i) {
        sum[i][j] += sum[i - 1][j];
      }
      if (0 < j) {
        sum[i][j] += sum[i][j - 1];
      }
      if (0 < i && 0 < j) {
        sum[i][j] -= sum[i - 1][j - 1];
      }
    }
  }

  for (int i = 0; i < N; i++) {
    int y, x;
    cin >> y >> x;
    y--;
    x--;
    cout << sum[y][x] << endl;
  }
}