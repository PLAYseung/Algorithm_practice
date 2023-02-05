public class fstSolution {

    String id;

    public fstSolution(String org) {
        this.id = solution(org);
    }

    public String solution(String new_id){

        new_id = new_id.toLowerCase();
        new_id = new_id.replaceAll("[^\\w-._]*","");
        new_id = new_id.replaceAll("[.]+",".");
        new_id = new_id.replaceAll("^[.]|[.]$","");
        if (new_id.length() > 15){
            new_id = new_id.substring(0,15).replaceAll("[.]$","");;
        }
        if (new_id.length()==0){
            new_id = "a";
        }
        if (new_id.length() < 3){
            while (new_id.length() < 3) {
                new_id += new_id.charAt(new_id.length() - 1);
            }
        }

        return new_id;
    }
}
