from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (True):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("************************************MENU**************************************")
    print("** 1. Thêm Sinh viên.")
    print("** 2. Cập nhật thông tin sinh viên bang ID")
    print("** 3. Xoa sinh vien boi ID.")
    print("** 4. Tim kiem sinh vien theo ten.")
    print("** 5. Sap xep sinh vien theo diem trung binh")
    print("** 6. Sap xep sinh vien theo ten chuye nganh")
    print("** 7. Hien thi danh sach sinh vien.")
    print("** 0. Thoat")
    print("*****************************************************************************")

    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("\nThem Sinh Vien Thanh Cong")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien. ")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSinhVien (ID)
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien. ")
            print("\nNhap ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("Sinh Vien co ID " + ID + " da bi xoa")
            else:
                print("\nSinh vien co Id = ", ID, " khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findByName (name)
            qlsv.showSinhVien (searchResult)
        else:
            print("\nDanh sach sinh vien trong")

    elif (key == 5):
        if (qlsv.soLuongSinhVien () > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh GPA.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
             print("\nDanh sach sinh vien trong")

    elif (key == 6):
        if (qlsv.soLuongSinhVien () > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh GPA.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong")

    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong")

    elif key == 0:
        print("\nThoat chuong trinh!")
        break
    else:
        print("\nChuc nang khong hop le, vui long nhap lai.")