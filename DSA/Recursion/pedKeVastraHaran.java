import java.util.*;

public class pedKeVastraHaran {
	public static void main(TreeNode node) {
		ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
		height(node,ans);

	}

	// hint along with assserting do the sorting on the way;
	public int height(TreeNode root,ArrayList<>() ans){
		if(root==null)	return -1;
		int l = height(root.left);
		int r = height(root.right);
		kint h = Math.max(l,r)+1;
		if(ans.size()==h) ans.add(new ArrayList<>())
		ans.get[h].add(root.val);
		return h;
    	}

}
