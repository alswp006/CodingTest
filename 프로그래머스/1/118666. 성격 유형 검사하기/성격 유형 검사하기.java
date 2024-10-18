class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        int[] rt = new int[]{0, 0};
        int[] cf = new int[]{0, 0};
        int[] jm = new int[]{0, 0};
        int[] an = new int[]{0, 0};

        for (int i = 0; i < survey.length; i++) {
            switch (survey[i]) {
                case "RT":
                    switch (choices[i]) {
                        case 1: rt[0] += 3; break;
                        case 2: rt[0] += 2; break;
                        case 3: rt[0] += 1; break;
                        case 4: rt[0] += 0; break;
                        case 5: rt[1] += 1; break;
                        case 6: rt[1] += 2; break;
                        case 7: rt[1] += 3; break;
                    }
                    break;
                case "TR":
                    switch (choices[i]) {
                        case 1: rt[1] += 3; break;
                        case 2: rt[1] += 2; break;
                        case 3: rt[1] += 1; break;
                        case 4: rt[1] += 0; break;
                        case 5: rt[0] += 1; break;
                        case 6: rt[0] += 2; break;
                        case 7: rt[0] += 3; break;
                    }
                    break;
                case "CF":
                    switch (choices[i]) {
                        case 1: cf[0] += 3; break;
                        case 2: cf[0] += 2; break;
                        case 3: cf[0] += 1; break;
                        case 4: cf[0] += 0; break;
                        case 5: cf[1] += 1; break;
                        case 6: cf[1] += 2; break;
                        case 7: cf[1] += 3; break;
                    }
                    break;
                case "FC":
                    switch (choices[i]) {
                        case 1: cf[1] += 3; break;
                        case 2: cf[1] += 2; break;
                        case 3: cf[1] += 1; break;
                        case 4: cf[1] += 0; break;
                        case 5: cf[0] += 1; break;
                        case 6: cf[0] += 2; break;
                        case 7: cf[0] += 3; break;
                    }
                    break;
                case "JM":
                    switch (choices[i]) {
                        case 1: jm[0] += 3; break;
                        case 2: jm[0] += 2; break;
                        case 3: jm[0] += 1; break;
                        case 4: jm[0] += 0; break;
                        case 5: jm[1] += 1; break;
                        case 6: jm[1] += 2; break;
                        case 7: jm[1] += 3; break;
                    }
                    break;
                case "MJ":
                    switch (choices[i]) {
                        case 1: jm[1] += 3; break;
                        case 2: jm[1] += 2; break;
                        case 3: jm[1] += 1; break;
                        case 4: jm[1] += 0; break;
                        case 5: jm[0] += 1; break;
                        case 6: jm[0] += 2; break;
                        case 7: jm[0] += 3; break;
                    }
                    break;
                case "AN":
                    switch (choices[i]) {
                        case 1: an[0] += 3; break;
                        case 2: an[0] += 2; break;
                        case 3: an[0] += 1; break;
                        case 4: an[0] += 0; break;
                        case 5: an[1] += 1; break;
                        case 6: an[1] += 2; break;
                        case 7: an[1] += 3; break;
                    }
                    break;
                case "NA":
                    switch (choices[i]) {
                        case 1: an[1] += 3; break;
                        case 2: an[1] += 2; break;
                        case 3: an[1] += 1; break;
                        case 4: an[1] += 0; break;
                        case 5: an[0] += 1; break;
                        case 6: an[0] += 2; break;
                        case 7: an[0] += 3; break;
                    }
                    break;
            }
        }

        // 각 점수를 비교하여 답 생성
        answer += rt[0] >= rt[1] ? "R" : "T";
        answer += cf[0] >= cf[1] ? "C" : "F";
        answer += jm[0] >= jm[1] ? "J" : "M";
        answer += an[0] >= an[1] ? "A" : "N";

        return answer;
    }
}