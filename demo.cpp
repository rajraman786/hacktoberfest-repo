#include<bits/stdc++.h>

using namespace std;
#define vt vector
#define ll long long

int main(){
	ll m1,m2;
	cin>>m1>>m2;
	ll n;
	cin>>n;
	vt<ll> a(n);
	ll s=0;
	for(int i=0;i<n;i++){
		cin>>a[i];
		s+=a[i];
	}
	vt<vt<bool>> dp(n+1,vt<bool>(s+1,0));
	vt<vt<bool>> dp1(n+1,vt<bool>(s+1,0)); // stores if current value adds to answer or not 
	// first -> 
	for(int i=0;i<n+1;i++){
		dp[i][0]=1;
	}
	for(int i=1;i<n+1;i++){
		for(int j=1;j<s+1;j++){
			if(j<a[i-1]){
				dp[i][j] = dp[i-1][j];
				dp1[i][j]=0;
			}
			else{
				if(dp[i-1][j]==1)
					dp1[i][j]=0;
				if(dp[i-1][j-a[i-1]]==1)
					dp1[i][j]=1;
				dp[i][j] = dp[i-1][j] || dp[i-1][j-a[i-1]];
			}
		}
	}
	// for(int i=0;i<n+1;i++){
	// 	for(int j=0;j<s+1;j++){
	// 		cout<<dp[i][j]<<" ";
	// 	}
	// 	cout<<"\n";
	// }
	ll m=INT_MAX,j=-1;
	for(int i=0;i<s+1;i++){
		if(dp[n][i]==1){
			if(m>max(m1*i,m2*(s-i))){
				m=max(m1*i,m2*(s-i));
				j=i;
			}
		}
	}
	vt<ll> fans1,fans2;
	ll i=n;
	for(int i=n;i>0;i--){
		if(dp1[i][j]){
			fans1.push_back(a[i-1]);
			j-=a[i-1];
		}
	}
	ll p1=0;
	sort(a.begin(),a.end());
	sort(fans1.begin(),fans1.end());
	for(int i=0;i<a.size();i++){
		if(p1<fans1.size()&&a[i]==fans1[p1]){
			p1++;
		}
		else{
			fans2.push_back(a[i]);
		}
	}
	for(int i=0;i<fans1.size();i++){
		cout<<fans1[i]<<" ";
	}
	cout<<"\n";
	for(int i=0;i<fans2.size();i++){
		cout<<fans2[i]<<" ";
	}
	return 0;
}