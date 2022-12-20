public class Solution {
    public IList<string> FizzBuzz(int n) {
        IList<string> answer = Enumerable.Range(1, n)
            .Select(i => FizzOrBuzz(i))
            .ToList(); 

        return answer;
    }

    private string FizzOrBuzz(int i)
    {
        if (i % 15 == 0) return "FizzBuzz";
        else if (i % 3 == 0) return "Fizz";
        else if (i % 5 == 0) return "Buzz";

        return i.ToString();
    }
}
