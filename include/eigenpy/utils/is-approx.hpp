/*
* Copyright 2020 INRIA
*/

#ifndef __eigenpy_utils_scalar_is_approx_hpp__
#define __eigenpy_utils_scalar_is_approx_hpp__

#include <Eigen/Core>

namespace eigenpy
{
  template<typename MatrixType1, typename MatrixType2>
  inline EIGEN_DONT_INLINE bool is_approx(const MatrixType1 & mat1,
                                          const MatrixType2 & mat2,
                                          const typename MatrixType1::Scalar & prec)
  {
    return mat1.derived().isApprox(mat2.derived(),prec);
  }

  template<typename MatrixType1, typename MatrixType2>
  inline bool is_approx(const MatrixType1 & mat1, const MatrixType2 & mat2)
  {
    return is_approx(mat1,mat2,Eigen::NumTraits<typename MatrixType1::Scalar>::dummy_precision());
  }
}

#endif // ifndef __eigenpy_utils_scalar_is_approx_hpp__
