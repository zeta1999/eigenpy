//
// Copyright (c) 2019-2020 INRIA
//

#ifndef __eigenpy_version_hpp__
#define __eigenpy_version_hpp__

#include "eigenpy/config.hpp"

#include <string>

namespace eigenpy
{
  
  ///
  /// \brief Returns the current version of EigenPy as a string using
  ///        the following standard:
  ///        EIGENPY_MINOR_VERSION.EIGENPY_MINOR_VERSION.EIGENPY_PATCH_VERSION
  ///
  std::string EIGENPY_DLLEXPORT printVersion(const std::string & delimiter = ".");
  
  ///
  /// \brief Checks if the current version of EigenPy is at least the version provided
  ///        by the input arguments.
  ///
  /// \param[in] major_version Major version to check.
  /// \param[in] minor_version Minor version to check.
  /// \param[in] patch_version Patch version to check.
  ///
  /// \returns true if the current version of EigenPy is greater than the version provided
  ///        by the input arguments.
  ///
  bool EIGENPY_DLLEXPORT checkVersionAtLeast(unsigned int major_version,
                                             unsigned int minor_version,
                                             unsigned int patch_version);
}

#endif // __eigenpy_version_hpp__
