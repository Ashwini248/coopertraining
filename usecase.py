class chennai:
    def chenn():
       
        area=input("which Locality u want:1->kodambakkam 2->Anna nagar: ")
        print("city:Chennai")
        if area=="1":
           
            details=["Locality:kodambakkam","square_feet:798","Type:2BHK","Rent:Rs.6000/mon","owner_id=1"]
            for i in details:
                print(i)
        elif area=="2":
            details=["Locality:Anna nagar","square_feet:1200","Type:3BHK","Rent:Rs.15000/mon","owner_id=2"]
           
            for i in details:
                print(i)
   
class  availability:
    def avail():
        place=input("which city u want:1->chennai 2->madurai: ")
        if place=="1":
            valid=chennai
            root=valid.chenn()
       
       
       
        elif place=="2":
            print("city:Madurai")
            details=["Locality:Goripalayam","square_feet:560","Type:1BHK" ,"Rent:Rs.5500/mon","owner_id=1"]
            for i in details:
                print(i)
       
       
   
if __name__=="__main__":
    who_u_r=input("if u are tenant put->T or if u are owner put->O or if u are approver put->A: ")
    if who_u_r=="T":
        check=availability
        state=check.avail()