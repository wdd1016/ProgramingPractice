#include <stdio.h>
#include <stdlib.h>

static void update_rev(int start, int end, int index, int left, int right,
                       int *tree, int *lazy);
static int sum_tree(int start, int end, int index, int left, int right,
                    int *tree, int *lazy);
static void update_lazy(int start, int end, int index, int *tree, int *lazy);

int main() {
  int s_count, w_count;     // s_count : switch 개수, w_count : 일의 수
  int inf, left, right, k;  // inf : 0 or 1

  scanf("%d %d", &s_count, &w_count);

  int tree[4 * s_count];  // make tree, arr <- all 0
  int lazy[4 * s_count];
  //	int arr[s_count] = { 값들 };

  //	init(0, s_count - 1, 1, arr, tree);
  for (int i = 0; i < 4 * s_count; i++) {
    tree[i] = 0;
    lazy[i] = 0;
  }
  for (int j = 0; j < w_count; j++) {
    scanf("%d %d %d", &inf, &left, &right);
    if (inf == 0)
      update_rev(1, s_count, 1, left, right, tree, lazy);
    else
      printf("%d\n", sum_tree(1, s_count, 1, left, right, tree, lazy));
  }
  return 0;
}

static void update_rev(
    int start, int end, int index, int left, int right, int *tree,
    int *lazy)  // start, end : 함수내 시작과 끝 arr[]idx, left, right : 판별
                // 기준 arr[]idx, index : 현재 tree[]idx
{
  update_lazy(start, end, index, tree, lazy);
  if (right < start || end < left)  // 범위에 벗어나는 경우
    return;
  else if (left <= start &&
           end <= right)  // 함수범위가 기준범위내에 포함되는 경우
  {
    tree[index] = (end - start + 1) - tree[index];  // 해당 노드 반전
    if (start != end) {
      lazy[index * 2] += 1;  // 하위노드 lazy 추가
      lazy[index * 2 + 1] += 1;
    }
    return;
  } else {
    int mid = (start + end) / 2;
    update_rev(start, mid, index * 2, left, right, tree, lazy);
    update_rev(mid + 1, end, index * 2 + 1, left, right, tree, lazy);
    tree[index] = tree[index * 2] + tree[index * 2 + 1];
    return;
  }
}

static int sum_tree(int start, int end, int index, int left, int right,
                    int *tree, int *lazy) {
  update_lazy(start, end, index, tree, lazy);
  if (right < start || end < left)  // 함수범위가 기준범위에서 벗어나는 경우
    return 0;
  else if (left <= start &&
           end <= right)  // 함수범위가 기준범위내에 포함되는 경우
    return tree[index];
  else {
    int mid = (start + end) / 2;
    return (sum_tree(start, mid, index * 2, left, right, tree, lazy) +
            sum_tree(mid + 1, end, index * 2 + 1, left, right, tree, lazy));
  }
}

static void update_lazy(int start, int end, int index, int *tree, int *lazy) {
  if (lazy[index] % 2 == 1)  // 값에 lazy적용
    tree[index] = (end - start + 1) - tree[index];
  if (start != end) {
    lazy[index * 2] += lazy[index];
    lazy[index * 2 + 1] += lazy[index];
  }
  lazy[index] = 0;  // lazy를 물려주므로 이제 0의 값을 가짐
}

/* 아래 내용은 lazy_Propagation이 구현되지 않아, 타임에러가 발생
static int	update_rev(int start, int end, int index, int left, int right,
int *tree)
// start, end : 함수내 시작과 끝 arr[]idx, left, right : 판별 기준 arr[]idx,
index : 현재 tree[]idx
{
        if (right < start || end < left) // 범위에 벗어나는 경우
                return tree[index];
        else if (start == end) // 끝에 도달하는 경우
        {
                tree[index] = !tree[index];
                return tree[index];
        }
        else
        {
                int mid = (start + end) / 2;
                tree[index] = update_rev(start, mid, index * 2, left, right,
tree) + \ update_rev(mid + 1, end, index * 2 + 1, left, right, tree); return
tree[index];
        }
}

static int sum_tree(int start, int end, int index, int left, int right, int
*tree)
{
        if (right < start || end < left) // 함수범위가 기준범위에서 벗어나는
경우 return 0; else if (left <= start && end <= right) // 함수범위가
기준범위내에 포함되는 경우 return tree[index]; else
        {
                int mid = (start + end) / 2;
                tree[index] = sum_tree(start, mid, index * 2, left, right, tree)
+ \ sum_tree(mid + 1, end, index * 2 + 1, left, right, tree); return
tree[index];
        }
}
*/

/*
int init(int start, int end, int index, int *arr, int *tree)
{
        if (start == end)
        {
                tree[index] = arr[start];
                return tree[index];
        }
        else
        {
                int mid = (start + end) / 2;
                tree[index] = init(start, mid, index * 2, arr, tree) + \
                init(mid + 1, end, index * 2 + 1, arr, tree);
                return tree[index];
        }
}
*/

/*
[자료구조] 세그먼트 트리 (Segment Tree)
https://velog.io/@kimdukbae/자료구조-세그먼트-트리-Segment-Tree
https://www.acmicpc.net/blog/view/9

[ Lazy Propagation ] 개념과 구현방법 (C++)
https://yabmoons.tistory.com/442

lazy update를 진행하고
새로운 update, scan을 진행중에 lazy노드를 터치하고, 해당부분 자손트리로
이전한다면 즉시 lazy를 해제하고 새로운 업데이트에 맞추어 새로운 lazy를 찾아
진행한다.
*/
