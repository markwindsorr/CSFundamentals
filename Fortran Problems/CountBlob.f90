PROGRAM CountBlob
!--------------------------------------------------------------------------
! Mark Windsor
!
! Count Blobs in matrix
!
!--------------------------------------------------------------------------

IMPLICIT NONE

integer :: m, n, result
integer, dimension(:, :), allocatable :: A

print *, "how many rows: "
read *, m

print *, "how many columns: "
read *, n

allocate(A(m, n))

result = Count(A, m, n)

contains
integer function Count(A, m, n)

integer, dimension(:, :), intent(in) :: A
integer, intent(in) :: m, n
integer :: count

count = 0

do while ()




end function



END PROGRAM CountBlob
