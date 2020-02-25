from ctypes import CDLL, CFUNCTYPE, POINTER, Structure, byref, pointer, create_string_buffer, string_at, cast
from ctypes import c_uint, c_char_p, c_bool, c_int, c_float, c_ubyte, c_void_p
from enum import IntEnum, IntFlag
from os import path
from typing import Callable, Any, Tuple
import sys


class _CEnum(IntEnum):
    @classmethod
    def from_param(cls, obj: '_CEnum') -> int:
        return int(obj)


class _CFlag(IntFlag):
    @classmethod
    def from_param(cls, obj: '_CFlag') -> int:
        return int(obj)


class VTFLibOption(_CEnum):
    VTFLIB_DXT_QUALITY = 0
    VTFLIB_LUMINANCE_WEIGHT_R = 1
    VTFLIB_LUMINANCE_WEIGHT_G = 2
    VTFLIB_LUMINANCE_WEIGHT_B = 3

    VTFLIB_BLUESCREEN_MASK_R = 4
    VTFLIB_BLUESCREEN_MASK_G = 5
    VTFLIB_BLUESCREEN_MASK_B = 6

    VTFLIB_BLUESCREEN_CLEAR_R = 7
    VTFLIB_BLUESCREEN_CLEAR_G = 8
    VTFLIB_BLUESCREEN_CLEAR_B = 9

    VTFLIB_FP16_HDR_KEY = 10
    VTFLIB_FP16_HDR_SHIFT = 11
    VTFLIB_FP16_HDR_GAMMA = 12

    VTFLIB_UNSHARPEN_RADIUS = 13
    VTFLIB_UNSHARPEN_AMOUNT = 14
    VTFLIB_UNSHARPEN_THRESHOLD = 15

    VTFLIB_XSHARPEN_STRENGTH = 16
    VTFLIB_XSHARPEN_THRESHOLD = 17

    VTFLIB_VMT_PARSE_MODE = 18


class VTFImageFormat(_CEnum):
    IMAGE_FORMAT_RGBA8888 = 0
    IMAGE_FORMAT_ABGR8888 = 1
    IMAGE_FORMAT_RGB888 = 2
    IMAGE_FORMAT_BGR888 = 3
    IMAGE_FORMAT_RGB565 = 4
    IMAGE_FORMAT_I8 = 5
    IMAGE_FORMAT_IA88 = 6
    IMAGE_FORMAT_P8 = 7
    IMAGE_FORMAT_A8 = 8
    IMAGE_FORMAT_RGB888_BLUESCREEN = 9
    IMAGE_FORMAT_BGR888_BLUESCREEN = 10
    IMAGE_FORMAT_ARGB8888 = 11
    IMAGE_FORMAT_BGRA8888 = 12
    IMAGE_FORMAT_DXT1 = 13
    IMAGE_FORMAT_DXT3 = 14
    IMAGE_FORMAT_DXT5 = 15
    IMAGE_FORMAT_BGRX8888 = 16
    IMAGE_FORMAT_BGR565 = 17
    IMAGE_FORMAT_BGRX5551 = 18
    IMAGE_FORMAT_BGRA4444 = 19
    IMAGE_FORMAT_DXT1_ONEBITALPHA = 20
    IMAGE_FORMAT_BGRA5551 = 21
    IMAGE_FORMAT_UV88 = 22
    IMAGE_FORMAT_UVWQ8888 = 23
    IMAGE_FORMAT_RGBA16161616F = 24
    IMAGE_FORMAT_RGBA16161616 = 25
    IMAGE_FORMAT_UVLX8888 = 26
    IMAGE_FORMAT_R32F = 27
    IMAGE_FORMAT_RGB323232F = 28
    IMAGE_FORMAT_RGBA32323232F = 29
    IMAGE_FORMAT_NV_DST16 = 30
    IMAGE_FORMAT_NV_DST24 = 31
    IMAGE_FORMAT_NV_INTZ = 32
    IMAGE_FORMAT_NV_RAWZ = 33
    IMAGE_FORMAT_ATI_DST16 = 34
    IMAGE_FORMAT_ATI_DST24 = 35
    IMAGE_FORMAT_NV_NULL = 36
    IMAGE_FORMAT_ATI2N = 37
    IMAGE_FORMAT_ATI1N = 38
    IMAGE_FORMAT_COUNT = 39
    IMAGE_FORMAT_NONE = -1


class VTFImageFlag(_CFlag):
    TEXTUREFLAGS_POINTSAMPLE = 0x00000001
    TEXTUREFLAGS_TRILINEAR = 0x00000002
    TEXTUREFLAGS_CLAMPS = 0x00000004
    TEXTUREFLAGS_CLAMPT = 0x00000008
    TEXTUREFLAGS_ANISOTROPIC = 0x00000010
    TEXTUREFLAGS_HINT_DXT5 = 0x00000020
    TEXTUREFLAGS_SRGB = 0x00000040
    TEXTUREFLAGS_DEPRECATED_NOCOMPRESS = 0x00000040
    TEXTUREFLAGS_NORMAL = 0x00000080
    TEXTUREFLAGS_NOMIP = 0x00000100
    TEXTUREFLAGS_NOLOD = 0x00000200
    TEXTUREFLAGS_MINMIP = 0x00000400
    TEXTUREFLAGS_PROCEDURAL = 0x00000800
    TEXTUREFLAGS_ONEBITALPHA = 0x00001000
    TEXTUREFLAGS_EIGHTBITALPHA = 0x00002000
    TEXTUREFLAGS_ENVMAP = 0x00004000
    TEXTUREFLAGS_RENDERTARGET = 0x00008000
    TEXTUREFLAGS_DEPTHRENDERTARGET = 0x00010000
    TEXTUREFLAGS_NODEBUGOVERRIDE = 0x00020000
    TEXTUREFLAGS_SINGLECOPY = 0x00040000
    TEXTUREFLAGS_UNUSED0 = 0x00080000
    TEXTUREFLAGS_DEPRECATED_ONEOVERMIPLEVELINALPHA = 0x00080000
    TEXTUREFLAGS_UNUSED1 = 0x00100000
    TEXTUREFLAGS_DEPRECATED_PREMULTCOLORBYONEOVERMIPLEVEL = 0x00100000
    TEXTUREFLAGS_UNUSED2 = 0x00200000
    TEXTUREFLAGS_DEPRECATED_NORMALTODUDV = 0x00200000
    TEXTUREFLAGS_UNUSED3 = 0x00400000
    TEXTUREFLAGS_DEPRECATED_ALPHATESTMIPGENERATION = 0x00400000
    TEXTUREFLAGS_NODEPTHBUFFER = 0x00800000
    TEXTUREFLAGS_UNUSED4 = 0x01000000
    TEXTUREFLAGS_DEPRECATED_NICEFILTERED = 0x01000000
    TEXTUREFLAGS_CLAMPU = 0x02000000
    TEXTUREFLAGS_VERTEXTEXTURE = 0x04000000
    TEXTUREFLAGS_SSBUMP = 0x08000000
    TEXTUREFLAGS_UNUSED5 = 0x10000000
    TEXTUREFLAGS_DEPRECATED_UNFILTERABLE_OK = 0x10000000
    TEXTUREFLAGS_BORDER = 0x20000000
    TEXTUREFLAGS_DEPRECATED_SPECVAR_RED = 0x40000000
    TEXTUREFLAGS_DEPRECATED_SPECVAR_ALPHA = 0x80000000
    TEXTUREFLAGS_LAST = 0x20000000
    TEXTUREFLAGS_COUNT = 30


class VTFCubeMapFace(_CEnum):
    CUBEMAP_FACE_RIGHT = 0
    CUBEMAP_FACE_LEFT = 1
    CUBEMAP_FACE_BACK = 2
    CUBEMAP_FACE_FRONT = 3
    CUBEMAP_FACE_UP = 4
    CUBEMAP_FACE_DOWN = 5
    CUBEMAP_FACE_SPHERE_MAP = 6
    CUBEMAP_FACE_COUNT = 7


class VTFMipMapFilter(_CEnum):
    MIPMAP_FILTER_POINT = 0
    MIPMAP_FILTER_BOX = 1
    MIPMAP_FILTER_TRIANGLE = 2
    MIPMAP_FILTER_QUADRATIC = 3
    MIPMAP_FILTER_CUBIC = 4
    MIPMAP_FILTER_CATROM = 5
    MIPMAP_FILTER_MITCHELL = 6
    MIPMAP_FILTER_GAUSSIAN = 7
    MIPMAP_FILTER_SINC = 8
    MIPMAP_FILTER_BESSEL = 9
    MIPMAP_FILTER_HANNING = 10
    MIPMAP_FILTER_HAMMING = 11
    MIPMAP_FILTER_BLACKMAN = 12
    MIPMAP_FILTER_KAISER = 13
    MIPMAP_FILTER_COUNT = 14


class VTFSharpenFilter(_CEnum):
    SHARPEN_FILTER_NONE = 0
    SHARPEN_FILTER_NEGATIVE = 1
    SHARPEN_FILTER_LIGHTER = 2
    SHARPEN_FILTER_DARKER = 3
    SHARPEN_FILTER_CONTRASTMORE = 4
    SHARPEN_FILTER_CONTRASTLESS = 5
    SHARPEN_FILTER_SMOOTHEN = 6
    SHARPEN_FILTER_SHARPENSOFT = 7
    SHARPEN_FILTER_SHARPENMEDIUM = 8
    SHARPEN_FILTER_SHARPENSTRONG = 9
    SHARPEN_FILTER_FINDEDGES = 10
    SHARPEN_FILTER_CONTOUR = 11
    SHARPEN_FILTER_EDGEDETECT = 12
    SHARPEN_FILTER_EDGEDETECTSOFT = 13
    SHARPEN_FILTER_EMBOSS = 14
    SHARPEN_FILTER_MEANREMOVAL = 15
    SHARPEN_FILTER_UNSHARP = 16
    SHARPEN_FILTER_XSHARPEN = 17
    SHARPEN_FILTER_WARPSHARP = 18
    SHARPEN_FILTER_COUNT = 19


class VTFDXTQuality(_CEnum):
    DXT_QUALITY_LOW = 0
    DXT_QUALITY_MEDIUM = 1
    DXT_QUALITY_HIGH = 2
    DXT_QUALITY_HIGHEST = 3
    DXT_QUALITY_COUNT = 4


class VTFKernelFilter(_CEnum):
    KERNEL_FILTER_4X = 0
    KERNEL_FILTER_3X3 = 1
    KERNEL_FILTER_5X5 = 2
    KERNEL_FILTER_7X7 = 3
    KERNEL_FILTER_9X9 = 4
    KERNEL_FILTER_DUDV = 5
    KERNEL_FILTER_COUNT = 6


class VTFHeightConversionMethod(_CEnum):
    HEIGHT_CONVERSION_METHOD_ALPHA = 0
    HEIGHT_CONVERSION_METHOD_AVERAGE_RGB = 1
    HEIGHT_CONVERSION_METHOD_BIASED_RGB = 2
    HEIGHT_CONVERSION_METHOD_RED = 3
    HEIGHT_CONVERSION_METHOD_GREEN = 4
    HEIGHT_CONVERSION_METHOD_BLUE = 5
    HEIGHT_CONVERSION_METHOD_MAX_RGB = 6
    HEIGHT_CONVERSION_METHOD_COLORSPACE = 7
    HEIGHT_CONVERSION_METHOD_COUNT = 8


class VTFNormalAlphaResult(_CEnum):
    NORMAL_ALPHA_RESULT_NOCHANGE = 0
    NORMAL_ALPHA_RESULT_HEIGHT = 1
    NORMAL_ALPHA_RESULT_BLACK = 2
    NORMAL_ALPHA_RESULT_WHITE = 3
    NORMAL_ALPHA_RESULT_COUNT = 4


class VTFResizeMethod(_CEnum):
    RESIZE_NEAREST_POWER2 = 0
    RESIZE_BIGGEST_POWER2 = 1
    RESIZE_SMALLEST_POWER2 = 2
    RESIZE_SET = 3
    RESIZE_COUNT = 4


class VTFResourceEntryTypeFlag(_CFlag):
    RSRCF_HAS_NO_DATA_CHUNK = 0x02


class VMTParseMode(_CEnum):
    PARSE_MODE_STRICT = 0
    PARSE_MODE_LOOSE = 1
    PARSE_MODE_COUNT = 2


class VMTNodeType(_CEnum):
    NODE_TYPE_GROUP = 0
    NODE_TYPE_GROUP_END = 1
    NODE_TYPE_STRING = 2
    NODE_TYPE_INTEGER = 3
    NODE_TYPE_SINGLE = 4
    NODE_TYPE_COUNT = 5


class SVTFImageFormatInfo(Structure):
    lpName: bytes
    uiBitsPerPixel: int
    uiBytesPerPixel: int
    uiRedBitsPerPixel: int
    uiGreenBitsPerPixel: int
    uiBlueBitsPerPixel: int
    uiAlphaBitsPerPixel: int
    bIsCompressed: bool
    bIsSupported: bool
    _pack_ = 1
    _fields_ = [("lpName", c_char_p),
                ("uiBitsPerPixel", c_uint),
                ("uiBytesPerPixel", c_uint),
                ("uiRedBitsPerPixel", c_uint),
                ("uiGreenBitsPerPixel", c_uint),
                ("uiBlueBitsPerPixel", c_uint),
                ("uiAlphaBitsPerPixel", c_uint),
                ("bIsCompressed", c_bool),
                ("bIsSupported", c_bool)]


class SVTFCreateOptions(Structure):
    ImageFormat: VTFImageFormat
    uiFlags: int
    uiStartFrame: int
    sBumpScale: float
    bMipmaps: bool
    MipmapFilter: VTFMipMapFilter
    MipmapSharpenFilter: VTFSharpenFilter
    bThumbnail: bool
    bReflectivity: bool
    bResize: bool
    ResizeMethod: VTFResizeMethod
    ResizeFilter: VTFMipMapFilter
    ResizeSharpenFilter: VTFSharpenFilter
    uiResizeWidth: int
    uiResizeHeight: int
    bResizeClamp: bool
    uiResizeClampWidth: int
    uiResizeClampHeight: int
    bGammaCorrection: bool
    sGammaCorrection: float
    bNormalMap: bool
    KernelFilter: VTFKernelFilter
    HeightConversionMethod: VTFHeightConversionMethod
    NormalAlphaResult: VTFNormalAlphaResult
    bNormalMinimumZ: bool
    sNormalScale: float
    bNormalWrap: bool
    bNormalInvertX: bool
    bNormalInvertY: bool
    bNormalInvertZ: bool
    bSphereMap: bool
    _pack_ = 1
    _fields_ = [("uiVersion", c_uint * 2),
                ("ImageFormat", c_int),
                ("uiFlags", c_uint),
                ("uiStartFrame", c_uint),
                ("sBumpScale", c_float),
                ("sReflectivity", c_float * 3),
                ("bMipmaps", c_bool),
                ("MipmapFilter", c_int),
                ("MipmapSharpenFilter", c_int),
                ("bThumbnail", c_bool),
                ("bReflectivity", c_bool),
                ("bResize", c_bool),
                ("ResizeMethod", c_int),
                ("ResizeFilter", c_int),
                ("ResizeSharpenFilter", c_int),
                ("uiResizeWidth", c_uint),
                ("uiResizeHeight", c_uint),
                ("bResizeClamp", c_bool),
                ("uiResizeClampWidth", c_uint),
                ("uiResizeClampHeight", c_uint),
                ("bGammaCorrection", c_bool),
                ("sGammaCorrection", c_float),
                ("bNormalMap", c_bool),
                ("KernelFilter", c_int),
                ("HeightConversionMethod", c_int),
                ("NormalAlphaResult", c_int),
                ("bNormalMinimumZ", c_bool),
                ("sNormalScale", c_float),
                ("bNormalWrap", c_bool),
                ("bNormalInvertX", c_bool),
                ("bNormalInvertY", c_bool),
                ("bNormalInvertZ", c_bool),
                ("bSphereMap", c_bool)]


class SVTFTextureLODControlResource(Structure):
    ResolutionClampU: int
    ResolutionClampV: int
    _pack_ = 1
    _fields_ = [("ResolutionClampU", c_ubyte),
                ("ResolutionClampV", c_ubyte),
                ("Padding", c_ubyte * 2)]


class VLProc(_CEnum):
    PROC_READ_CLOSE = 0
    PROC_READ_OPEN = 1
    PROC_READ_READ = 2
    PROC_READ_SEEK = 3
    PROC_READ_TELL = 4
    PROC_READ_SIZE = 5
    PROC_WRITE_CLOSE = 6
    PROC_WRITE_OPEN = 7
    PROC_WRITE_WRITE = 8
    PROC_WRITE_SEEK = 9
    PROC_WRITE_SIZE = 10
    PROC_WRITE_TELL = 11
    PROC_COUNT = 12


class VLSeekMode(_CEnum):
    SEEK_MODE_BEGIN = 0
    SEEK_MODE_CURRENT = 1
    SEEK_MODE_END = 2


_is_64 = sys.maxsize > 2**32
_library_path = path.join(path.dirname(__file__), "bin", "x64" if _is_64 else "x86", "VTFLib.dll")

_vtflib = CDLL(_library_path)

_vl_get_version: Callable[[], int] = CFUNCTYPE(c_uint)(("vlGetVersion", _vtflib))
_vl_get_version_string: Callable[[], bytes] = CFUNCTYPE(c_char_p)(("vlGetVersionString", _vtflib))

_vl_get_last_error: Callable[[], bytes] = CFUNCTYPE(c_char_p)(("vlGetLastError", _vtflib))

_vl_initialize: Callable[[], bool] = CFUNCTYPE(c_bool)(("vlInitialize", _vtflib))
_vl_shutdown: Callable[[], None] = CFUNCTYPE(None)(("vlShutdown", _vtflib))

_vl_get_boolean: Callable[[VTFLibOption], bool] = CFUNCTYPE(c_bool, c_int)(("vlGetBoolean", _vtflib))
_vl_set_boolean: Callable[[VTFLibOption, bool], None] = CFUNCTYPE(None, c_int, c_bool)(("vlSetBoolean", _vtflib))

_vl_get_integer: Callable[[VTFLibOption], int] = CFUNCTYPE(c_int, c_int)(("vlGetInteger", _vtflib))
_vl_set_integer: Callable[[VTFLibOption, int], None] = CFUNCTYPE(None, c_int, c_int)(("vlSetInteger", _vtflib))

_vl_get_float: Callable[[VTFLibOption], float] = CFUNCTYPE(c_float, c_int)(("vlGetFloat", _vtflib))
_vl_set_float: Callable[[VTFLibOption, float], None] = CFUNCTYPE(None, c_int, c_float)(("vlSetFloat", _vtflib))

_vl_set_proc: Callable[[VLProc, int], None] = CFUNCTYPE(None, c_int, c_void_p)(("vlSetProc", _vtflib))
_vl_get_proc: Callable[[VLProc], int] = CFUNCTYPE(c_void_p, c_int)(("vlGetProc", _vtflib))

_vl_image_is_bound: Callable[[], bool] = CFUNCTYPE(c_bool)(("vlImageIsBound", _vtflib))
_vl_bind_image: Callable[[c_uint], bool] = CFUNCTYPE(c_bool, c_uint)(("vlBindImage", _vtflib))

_vl_create_image: Callable[[Any], bool] = CFUNCTYPE(c_bool, POINTER(c_uint))(("vlCreateImage", _vtflib))
_vl_delete_image: Callable[[c_uint], None] = CFUNCTYPE(None, c_uint)(("vlDeleteImage", _vtflib))

_vl_image_create_default_create_structure: Callable[[Any], None] = \
    CFUNCTYPE(None, POINTER(SVTFCreateOptions))(("vlImageCreateDefaultCreateStructure", _vtflib))

_vl_image_create: Callable[[int, int, int, int, int, VTFImageFormat, bool, bool, bool], bool] = \
    CFUNCTYPE(c_bool, c_uint, c_uint, c_uint, c_uint, c_uint, c_int, c_bool, c_bool, c_bool)(("vlImageCreate", _vtflib))
_vl_image_create_single: Callable[[int, int, Any, Any], bool] = \
    CFUNCTYPE(c_bool, c_uint, c_uint, c_char_p, POINTER(SVTFCreateOptions))(("vlImageCreateSingle", _vtflib))
_vl_image_create_multiple: Callable[[int, int, int, int, int, Any, Any], bool] = \
    CFUNCTYPE(c_bool, c_uint, c_uint, c_uint, c_uint, c_uint, POINTER(c_char_p), POINTER(SVTFCreateOptions))(
        ("vlImageCreateMultiple", _vtflib))
_vl_image_destroy: Callable[[], None] = CFUNCTYPE(None)(("vlImageDestroy", _vtflib))

_vl_image_is_loaded: Callable[[], bool] = CFUNCTYPE(c_bool)(("vlImageIsLoaded", _vtflib))

_vl_image_load: Callable[[bytes, bool], bool] = CFUNCTYPE(c_bool, c_char_p, c_bool)(("vlImageLoad", _vtflib))
_vl_image_load_lump: Callable[[c_void_p, int, bool], bool] = CFUNCTYPE(c_bool, c_void_p, c_uint, c_bool)(
    ("vlImageLoadLump", _vtflib))
_vl_image_load_proc: Callable[[int, bool], bool] = CFUNCTYPE(c_bool, c_void_p, c_bool)(("vlImageLoadProc", _vtflib))

_vl_image_save: Callable[[bytes], bool] = CFUNCTYPE(c_bool, c_char_p)(("vlImageSave", _vtflib))
_vl_image_save_lump: Callable[[c_void_p, int, Any], bool] = CFUNCTYPE(c_bool, c_void_p, c_uint, POINTER(c_uint))(
    ("vlImageSaveLump", _vtflib))
_vl_image_save_proc: Callable[[int], bool] = CFUNCTYPE(c_bool, c_void_p)(("vlImageSaveProc", _vtflib))

_vl_image_get_has_image: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetHasImage", _vtflib))

_vl_image_get_major_version: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetMajorVersion", _vtflib))
_vl_image_get_minor_version: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetMinorVersion", _vtflib))
_vl_image_get_size: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetSize", _vtflib))

_vl_image_get_width: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetWidth", _vtflib))
_vl_image_get_height: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetHeight", _vtflib))
_vl_image_get_depth: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetDepth", _vtflib))

_vl_image_get_frame_count: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetFrameCount", _vtflib))
_vl_image_get_face_count: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetFaceCount", _vtflib))
_vl_image_get_mipmap_count: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetMipmapCount", _vtflib))

_vl_image_get_start_frame: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetStartFrame", _vtflib))
_vl_image_set_start_frame: Callable[[int], None] = CFUNCTYPE(None, c_uint)(("vlImageSetStartFrame", _vtflib))

_vl_image_get_flags: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetFlags", _vtflib))
_vl_image_set_flags: Callable[[int], None] = CFUNCTYPE(None, c_uint)(("vlImageSetFlags", _vtflib))

_vl_image_get_flag: Callable[[VTFImageFlag], bool] = CFUNCTYPE(c_bool, c_int)(("vlImageGetFlag", _vtflib))
_vl_image_set_flag: Callable[[VTFImageFlag, bool], None] = CFUNCTYPE(None, c_int, c_bool)(("vlImageSetFlag", _vtflib))

_vl_image_get_bumpmap_scale: Callable[[], float] = CFUNCTYPE(c_float)(("vlImageGetBumpmapScale", _vtflib))
_vl_image_set_bumpmap_scale: Callable[[float], None] = CFUNCTYPE(None, c_float)(("vlImageSetBumpmapScale", _vtflib))

_vl_image_get_reflectivity: Callable[[Any, Any, Any], None] = \
    CFUNCTYPE(None, POINTER(c_float), POINTER(c_float), POINTER(c_float))(("vlImageGetReflectivity", _vtflib))
_vl_image_set_reflectivity: Callable[[float, float, float], None] = CFUNCTYPE(None, c_float, c_float, c_float)(
    ("vlImageSetReflectivity", _vtflib))

_vl_image_get_format: Callable[[], int] = CFUNCTYPE(c_int)(("vlImageGetFormat", _vtflib))

_vl_image_get_data: Callable[[int, int, int, int], Any] = CFUNCTYPE(POINTER(c_ubyte), c_uint, c_uint, c_uint, c_uint)(
    ("vlImageGetData", _vtflib))
_vl_image_set_data: Callable[[int, int, int, int, Any], None] = \
    CFUNCTYPE(None, c_uint, c_uint, c_uint, c_uint, c_char_p)(("vlImageSetData", _vtflib))

_vl_image_get_has_thumbnail: Callable[[], bool] = CFUNCTYPE(c_bool)(("vlImageGetHasThumbnail", _vtflib))
_vl_image_get_thumbnail_width: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetThumbnailWidth", _vtflib))
_vl_image_get_thumbnail_height: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetThumbnailHeight", _vtflib))

_vl_image_get_thumbnail_format: Callable[[], int] = CFUNCTYPE(c_int)(("vlImageGetThumbnailFormat", _vtflib))

_vl_image_get_thumbnail_data: Callable[[], Any] = CFUNCTYPE(POINTER(c_ubyte))(("vlImageGetThumbnailData", _vtflib))
_vl_image_set_thumbnail_data: Callable[[Any], None] = CFUNCTYPE(None, c_char_p)(
    ("vlImageSetThumbnailData", _vtflib))

_vl_image_get_supports_resources: Callable[[], bool] = CFUNCTYPE(c_bool)(("vlImageGetSupportsResources", _vtflib))

_vl_image_get_resource_count: Callable[[], int] = CFUNCTYPE(c_uint)(("vlImageGetResourceCount", _vtflib))
_vl_image_get_resource_type: Callable[[int], int] = CFUNCTYPE(c_uint, c_uint)(("vlImageGetResourceType", _vtflib))
_vl_image_get_has_resource: Callable[[int], bool] = CFUNCTYPE(c_bool, c_uint)(("vlImageGetHasResource", _vtflib))

_vl_image_get_resource_data: Callable[[int, Any], int] = CFUNCTYPE(c_void_p, c_uint, POINTER(c_uint))(
    ("vlImageGetResourceData", _vtflib))
_vl_image_set_resource_data: Callable[[int, int, int], int] = CFUNCTYPE(c_void_p, c_uint, c_uint, c_void_p)(
    ("vlImageSetResourceData", _vtflib))

_vl_image_generate_mipmaps: Callable[[int, int, VTFMipMapFilter, VTFSharpenFilter], bool] = \
    CFUNCTYPE(c_bool, c_uint, c_uint, c_int, c_int)(("vlImageGenerateMipmaps", _vtflib))
_vl_image_generate_all_mipmaps: Callable[[VTFMipMapFilter, VTFSharpenFilter], bool] = \
    CFUNCTYPE(c_bool, c_int, c_int)(("vlImageGenerateAllMipmaps", _vtflib))

_vl_image_generate_thumbnail: Callable[[], bool] = CFUNCTYPE(c_bool)(("vlImageGenerateThumbnail", _vtflib))

_vl_image_generate_normal_map: Callable[[int, VTFKernelFilter, VTFHeightConversionMethod, VTFNormalAlphaResult], bool] \
    = CFUNCTYPE(c_bool, c_uint, c_int, c_int, c_int)(("vlImageGenerateNormalMap", _vtflib))
_vl_image_generate_all_normal_maps: Callable[[VTFKernelFilter, VTFHeightConversionMethod, VTFNormalAlphaResult], bool] \
    = CFUNCTYPE(c_bool, c_int, c_int, c_int)(("vlImageGenerateAllNormalMaps", _vtflib))

_vl_image_generate_sphere_map: Callable[[], bool] = CFUNCTYPE(c_bool)(("vlImageGenerateSphereMap", _vtflib))

_vl_image_compute_reflectivity: Callable[[], bool] = CFUNCTYPE(c_bool)(("vlImageComputeReflectivity", _vtflib))

_vl_image_get_image_format_info: Callable[[VTFImageFormat], Any] = CFUNCTYPE(POINTER(SVTFImageFormatInfo), c_int)(
    ("vlImageGetImageFormatInfo", _vtflib))
_vl_image_get_image_format_info_ex: Callable[[VTFImageFormat, Any], bool] = \
    CFUNCTYPE(c_bool, c_int, POINTER(SVTFImageFormatInfo))(("vlImageGetImageFormatInfoEx", _vtflib))

_vl_image_compute_image_size: Callable[[int, int, int, int, VTFImageFormat], int] = \
    CFUNCTYPE(c_uint, c_uint, c_uint, c_uint, c_uint, c_int)(("vlImageComputeImageSize", _vtflib))

_vl_image_compute_mipmap_count: Callable[[int, int, int], int] = \
    CFUNCTYPE(c_uint, c_uint, c_uint, c_uint)(("vlImageComputeMipmapCount", _vtflib))
_vl_image_compute_mipmap_dimensions: Callable[[int, int, int, int, Any, Any, Any], None] = \
    CFUNCTYPE(None, c_uint, c_uint, c_uint, c_uint, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint))(
        ("vlImageComputeMipmapDimensions", _vtflib))
_vl_image_compute_mipmap_size: Callable[[int, int, int, int, VTFImageFormat], int] = \
    CFUNCTYPE(c_uint, c_uint, c_uint, c_uint, c_uint, c_int)(("vlImageComputeMipmapSize", _vtflib))

_vl_image_convert_to_rgba8888: Callable[[Any, Any, int, int, VTFImageFormat], bool] = \
    CFUNCTYPE(c_bool, c_char_p, c_char_p, c_uint, c_uint, c_int)(("vlImageConvertToRGBA8888", _vtflib))
_vl_image_convert_from_rgba8888: Callable[[Any, Any, int, int, VTFImageFormat], bool] = \
    CFUNCTYPE(c_bool, c_char_p, c_char_p, c_uint, c_uint, c_int)(
        ("vlImageConvertFromRGBA8888", _vtflib))

_vl_image_convert: Callable[[Any, Any, int, int, VTFImageFormat, VTFImageFormat], bool] = \
    CFUNCTYPE(c_bool, c_char_p, c_char_p, c_uint, c_uint, c_int, c_int)(("vlImageConvert", _vtflib))

_vl_image_convert_to_normal_map: Callable[[Any, Any, int, int, VTFKernelFilter, VTFHeightConversionMethod,
                                          VTFNormalAlphaResult, int, float, bool, bool, bool], bool] = \
    CFUNCTYPE(c_bool, c_char_p, c_char_p, c_uint, c_uint, c_int, c_int, c_int,
              c_ubyte, c_float, c_bool, c_bool, c_bool)(("vlImageConvertToNormalMap", _vtflib))

_vl_image_resize: Callable[[Any, Any, int, int, int, int, VTFMipMapFilter, VTFSharpenFilter], bool] = \
    CFUNCTYPE(c_bool, c_char_p, c_char_p, c_uint, c_uint, c_uint, c_uint, c_int, c_int)(
        ("vlImageResize", _vtflib))

_vl_image_correct_image_gamma: Callable[[Any, int, int, float], None] = \
    CFUNCTYPE(None, c_char_p, c_uint, c_uint, c_float)(("vlImageCorrectImageGamma", _vtflib))
_vl_image_compute_image_reflectivity: Callable[[Any, int, int, Any, Any, Any], None] = \
    CFUNCTYPE(None, c_char_p, c_uint, c_uint, POINTER(c_float), POINTER(c_float), POINTER(c_float))(
        ("vlImageComputeImageReflectivity", _vtflib))

_vl_image_flip_image: Callable[[Any, int, int], None] = \
    CFUNCTYPE(None, c_char_p, c_uint, c_uint)(("vlImageFlipImage", _vtflib))
_vl_image_mirror_image: Callable[[Any, int, int], None] = \
    CFUNCTYPE(None, c_char_p, c_uint, c_uint)(("vlImageMirrorImage", _vtflib))

# TODO implement VMT functions


class VTFException(Exception):
    def __init__(self) -> None:
        error = _vl_get_last_error().decode('mbcs')
        super().__init__(error)


class VTFLib():
    def __init__(self) -> None:
        self._image_handle = c_uint()
        _vl_initialize()
        if not _vl_create_image(byref(self._image_handle)):
            raise VTFException
        if not _vl_bind_image(self._image_handle):
            raise VTFException

    def close(self) -> None:
        _vl_delete_image(self._image_handle)
        _vl_shutdown()

    def __enter__(self) -> 'VTFLib':
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        self.close()

    @staticmethod
    def get_version() -> int:
        return _vl_get_version()

    @staticmethod
    def get_version_str() -> str:
        return _vl_get_version_string().decode('mbcs')

    def create_image(self, width: int, height: int, frames: int = 1, faces: int = 1, slices: int = 1,
                     img_format: VTFImageFormat = VTFImageFormat.IMAGE_FORMAT_RGBA8888, thumbnail: bool = True,
                     mipmaps: bool = True, null_data: bool = False) -> None:
        if not _vl_image_create(width, height, frames, faces, slices, img_format, thumbnail, mipmaps, null_data):
            raise VTFException

    def destroy_image(self) -> None:
        _vl_image_destroy()

    def is_image_loaded(self) -> bool:
        return _vl_image_is_loaded()

    def load_image_file(self, path: str, header_only: bool = False) -> None:
        if not _vl_image_load(path.encode('mbcs'), header_only):
            raise VTFException

    def load_image_bytes(self, data: bytes, header_only: bool = False) -> None:
        buffer = create_string_buffer(data)
        if not _vl_image_load_lump(cast(buffer, c_void_p), len(buffer), header_only):
            raise VTFException

    def save_image_file(self, path: str) -> None:
        if not _vl_image_save(path.encode('mbcs')):
            raise VTFException

    def save_image_bytes(self) -> bytes:
        size = _vl_image_get_size()
        buffer = create_string_buffer(size)
        if not _vl_image_save_lump(cast(buffer, c_void_p), size, pointer(c_uint())):
            raise VTFException
        return buffer.raw

    def image_has_image(self) -> bool:
        return bool(_vl_image_get_has_image())

    def image_major_version(self) -> int:
        return _vl_image_get_major_version()

    def image_minor_version(self) -> int:
        return _vl_image_get_minor_version()

    def image_size(self) -> int:
        return _vl_image_get_size()

    def image_width(self) -> int:
        return _vl_image_get_width()

    def image_height(self) -> int:
        return _vl_image_get_height()

    def image_depth(self) -> int:
        return _vl_image_get_depth()

    def image_frame_count(self) -> int:
        return _vl_image_get_frame_count()

    def image_face_count(self) -> int:
        return _vl_image_get_face_count()

    def image_mipmap_count(self) -> int:
        return _vl_image_get_mipmap_count()

    def image_start_frame(self) -> int:
        return _vl_image_get_start_frame()

    def image_set_start_frame(self, frame: int) -> None:
        _vl_image_set_start_frame(frame)

    def image_flags(self) -> int:
        return _vl_image_get_flags()

    def image_set_flags(self, flags: int) -> None:
        _vl_image_set_flags(flags)

    def image_get_flag(self, flag: VTFImageFlag) -> bool:
        return _vl_image_get_flag(flag)

    def image_set_flag(self, flag: VTFImageFlag, value: bool) -> None:
        _vl_image_set_flag(flag, value)

    def image_bumpmap_scale(self) -> float:
        return _vl_image_get_bumpmap_scale()

    def image_set_bumpmap_scale(self, scale: float) -> None:
        _vl_image_set_bumpmap_scale(scale)

    def image_reflectivity(self) -> Tuple[float, float, float]:
        x = c_float()
        y = c_float()
        z = c_float()
        _vl_image_get_reflectivity(byref(x), byref(y), byref(z))
        return (x.value, y.value, z.value)

    def image_set_reflectivity(self, x: float, y: float, z: float) -> None:
        _vl_image_set_reflectivity(x, y, z)

    def image_format(self) -> VTFImageFormat:
        return VTFImageFormat(_vl_image_get_format())

    def image_get_data(self, frame: int = 0, face: int = 0, z_slice: int = 0, mipmap_lvl: int = 0) -> bytes:
        data_pointer = _vl_image_get_data(frame, face, z_slice, mipmap_lvl)
        return string_at(data_pointer, self.compute_mipmap_size(self.image_width(), self.image_height(),
                                                                1, mipmap_lvl, self.image_format()))

    def image_set_data(self, data: bytes, frame: int = 0, face: int = 0, z_slice: int = 0, mipmap_lvl: int = 0) -> None:
        data_buffer = create_string_buffer(data, len(data))
        _vl_image_set_data(frame, face, z_slice, mipmap_lvl, data_buffer)

    def image_has_thumbnail(self) -> bool:
        return _vl_image_get_has_thumbnail()

    def image_thumbnail_width(self) -> int:
        return _vl_image_get_thumbnail_width()

    def image_thumbnail_height(self) -> int:
        return _vl_image_get_thumbnail_height()

    def image_thumbnail_format(self) -> VTFImageFormat:
        return VTFImageFormat(_vl_image_get_thumbnail_format())

    def image_thumbnail_data(self) -> bytes:
        data_pointer = _vl_image_get_thumbnail_data()
        return string_at(data_pointer, self.compute_image_size(self.image_thumbnail_width(),
                                                               self.image_thumbnail_height(),
                                                               1, 1, self.image_thumbnail_format()))

    def image_thumbnail_set_data(self, data: bytes) -> None:
        data_buffer = create_string_buffer(data, len(data))
        _vl_image_set_thumbnail_data(data_buffer)

    def image_supports_resources(self) -> bool:
        return _vl_image_get_supports_resources()

    def image_resource_count(self) -> int:
        return _vl_image_get_resource_count()

    def image_get_resouce_type(self, index: int) -> int:
        return _vl_image_get_resource_type(index)

    def image_get_has_resouce(self, resource_type: int) -> bool:
        return _vl_image_get_has_resource(resource_type)

    def image_generate_mipmaps(self, face: int, frame: int,
                               mipmap_filter: VTFMipMapFilter = VTFMipMapFilter.MIPMAP_FILTER_BOX,
                               sharpen_filter: VTFSharpenFilter = VTFSharpenFilter.SHARPEN_FILTER_NONE) -> None:
        if not _vl_image_generate_mipmaps(face, frame, mipmap_filter, sharpen_filter):
            raise VTFException

    def image_generate_all_mipmaps(self, mipmap_filter: VTFMipMapFilter = VTFMipMapFilter.MIPMAP_FILTER_BOX,
                                   sharpen_filter: VTFSharpenFilter = VTFSharpenFilter.SHARPEN_FILTER_NONE) -> None:
        if not _vl_image_generate_all_mipmaps(mipmap_filter, sharpen_filter):
            raise VTFException

    def image_generate_thumbnail(self) -> None:
        if not _vl_image_generate_thumbnail():
            raise VTFException

    def image_generate_normal_map(self, frame: int, kernel_filter: VTFKernelFilter = VTFKernelFilter.KERNEL_FILTER_3X3,
                                  height_conv: VTFHeightConversionMethod =
                                  VTFHeightConversionMethod.HEIGHT_CONVERSION_METHOD_AVERAGE_RGB,
                                  alpha_result: VTFNormalAlphaResult = VTFNormalAlphaResult.NORMAL_ALPHA_RESULT_WHITE
                                  ) -> None:
        if not _vl_image_generate_normal_map(frame, kernel_filter, height_conv, alpha_result):
            raise VTFException

    def image_generate_all_normal_maps(self, kernel_filter: VTFKernelFilter = VTFKernelFilter.KERNEL_FILTER_3X3,
                                       height_conv: VTFHeightConversionMethod =
                                       VTFHeightConversionMethod.HEIGHT_CONVERSION_METHOD_AVERAGE_RGB,
                                       alpha_result: VTFNormalAlphaResult =
                                       VTFNormalAlphaResult.NORMAL_ALPHA_RESULT_WHITE
                                       ) -> None:
        if not _vl_image_generate_all_normal_maps(kernel_filter, height_conv, alpha_result):
            raise VTFException

    def image_generate_sphere_map(self) -> None:
        if not _vl_image_generate_sphere_map():
            raise VTFException

    def image_compute_reflectivity(self) -> None:
        if not _vl_image_compute_reflectivity():
            raise VTFException

    @staticmethod
    def get_image_format_info(img_format: VTFImageFormat) -> SVTFImageFormatInfo:
        info_pointer = _vl_image_get_image_format_info(img_format)
        return info_pointer.contents

    @staticmethod
    def compute_image_size(width: int, height: int, depth: int, mipmaps: int, img_format: VTFImageFormat) -> int:
        return _vl_image_compute_image_size(width, height, depth, mipmaps, img_format)

    @staticmethod
    def compute_mipmap_count(width: int, height: int, depth: int) -> int:
        return _vl_image_compute_mipmap_count(width, height, depth)

    @staticmethod
    def compute_mipmap_dimensions(width: int, height: int, depth: int, mipmap_level: int) -> Tuple[int, int, int]:
        mipmap_w = c_uint()
        mipmap_h = c_uint()
        mipmap_d = c_uint()
        _vl_image_compute_mipmap_dimensions(width, height, depth, mipmap_level,
                                            byref(mipmap_w), byref(mipmap_h), byref(mipmap_d))
        return (mipmap_w.value, mipmap_h.value, mipmap_d.value)

    @staticmethod
    def compute_mipmap_size(width: int, height: int, depth: int, mipmap_level: int, img_format: VTFImageFormat
                            ) -> int:
        return _vl_image_compute_mipmap_size(width, height, depth, mipmap_level, img_format)

    @staticmethod
    def convert_to_rgba8888(source: bytes, width: int, height: int, source_format: VTFImageFormat) -> bytes:
        source_buffer = create_string_buffer(source, len(source))
        dest_buffer = create_string_buffer(
            _vl_image_compute_image_size(width, height, 1, 1, VTFImageFormat.IMAGE_FORMAT_RGBA8888)
        )
        if not _vl_image_convert_to_rgba8888(source_buffer, dest_buffer, width, height, source_format):
            raise VTFException
        return dest_buffer.raw

    @staticmethod
    def convert_from_rgba8888(source: bytes, width: int, height: int, dest_format: VTFImageFormat) -> bytes:
        source_buffer = create_string_buffer(source, len(source))
        dest_buffer = create_string_buffer(_vl_image_compute_image_size(width, height, 1, 1, dest_format))
        if not _vl_image_convert_from_rgba8888(source_buffer, dest_buffer, width, height, dest_format):
            raise VTFException
        return dest_buffer.raw

    @staticmethod
    def convert(source: bytes, width: int, height: int,
                source_format: VTFImageFormat, dest_format: VTFImageFormat) -> bytes:
        source_buffer = create_string_buffer(source, len(source))
        dest_buffer = create_string_buffer(_vl_image_compute_image_size(width, height, 1, 1, dest_format))
        if not _vl_image_convert(source_buffer, dest_buffer, width, height, source_format, dest_format):
            raise VTFException
        return dest_buffer.raw

    @staticmethod
    def convert_to_normal_map(source_rgba8888: bytes, width: int, height: int,
                              kernel_filter: VTFKernelFilter = VTFKernelFilter.KERNEL_FILTER_3X3,
                              height_conv: VTFHeightConversionMethod =
                              VTFHeightConversionMethod.HEIGHT_CONVERSION_METHOD_AVERAGE_RGB,
                              alpha_result: VTFNormalAlphaResult = VTFNormalAlphaResult.NORMAL_ALPHA_RESULT_WHITE,
                              min_z: int = 0, scale: float = 2., wrap: bool = False,
                              invert_x: bool = False, invert_y: bool = False) -> bytes:
        source_buffer = create_string_buffer(source_rgba8888, len(source_rgba8888))
        dest_buffer = create_string_buffer(
            _vl_image_compute_image_size(width, height, 1, 1, VTFImageFormat.IMAGE_FORMAT_RGBA8888)
        )
        if not _vl_image_convert_to_normal_map(source_buffer, dest_buffer, width, height, kernel_filter, height_conv,
                                               alpha_result, min_z, scale, wrap, invert_x, invert_y):
            raise VTFException
        return dest_buffer.raw

    @staticmethod
    def resize(source_rgba8888: bytes, source_width: int, source_height: int, dest_width: int, dest_height: int,
               resize_filter: VTFMipMapFilter = VTFMipMapFilter.MIPMAP_FILTER_TRIANGLE,
               sharpen_filter: VTFSharpenFilter = VTFSharpenFilter.SHARPEN_FILTER_NONE) -> bytes:
        source_buffer = create_string_buffer(source_rgba8888, len(source_rgba8888))
        dest_buffer = create_string_buffer(
            _vl_image_compute_image_size(dest_width, dest_height, 1, 1, VTFImageFormat.IMAGE_FORMAT_RGBA8888)
        )
        if not _vl_image_resize(source_buffer, dest_buffer, source_width, source_height, dest_width, dest_height,
                                resize_filter, sharpen_filter):
            raise VTFException
        return dest_buffer.raw

    @staticmethod
    def correct_image_gamma(source_rgba8888: bytes, width: int, height: int, gamma_correction: float) -> bytes:
        source_buffer = create_string_buffer(source_rgba8888, len(source_rgba8888))
        _vl_image_correct_image_gamma(source_buffer, width, height, gamma_correction)
        return source_buffer.raw

    @staticmethod
    def compute_image_reflectivity(source_rgba8888: bytes, width: int, height: int) -> Tuple[float, float, float]:
        x = c_float()
        y = c_float()
        z = c_float()
        source_buffer = create_string_buffer(source_rgba8888, len(source_rgba8888))
        _vl_image_compute_image_reflectivity(source_buffer, width, height, byref(x), byref(y), byref(z))
        return (x.value, y.value, z.value)

    @staticmethod
    def flip_image(source_rgba8888: bytes, width: int, height: int) -> bytes:
        source_buffer = create_string_buffer(source_rgba8888, len(source_rgba8888))
        _vl_image_flip_image(source_buffer, width, height)
        return source_buffer.raw

    @staticmethod
    def mirror_image(source_rgba8888: bytes, width: int, height: int) -> bytes:
        source_buffer = create_string_buffer(source_rgba8888, len(source_rgba8888))
        _vl_image_mirror_image(source_buffer, width, height)
        return source_buffer.raw

    # convenience additions

    def image_as_rgba8888(self, frame: int = 0, face: int = 0, z_slice: int = 0, mipmap_lvl: int = 0) -> bytes:
        if self.image_format() == VTFImageFormat.IMAGE_FORMAT_RGBA8888:
            return self.image_get_data(frame, face, z_slice, mipmap_lvl)
        data_pointer = _vl_image_get_data(frame, face, z_slice, mipmap_lvl)
        width, height, _ = self.compute_mipmap_dimensions(self.image_width(), self.image_height(), 1, mipmap_lvl)
        dest_buffer = create_string_buffer(
            _vl_image_compute_image_size(width, height, 1, 1, VTFImageFormat.IMAGE_FORMAT_RGBA8888)
        )
        if not _vl_image_convert_to_rgba8888(cast(data_pointer, c_char_p), dest_buffer,
                                             width, height, self.image_format()):
            raise VTFException
        return dest_buffer.raw

    def image_from_rgba8888(self, data: bytes, frame: int = 0, face: int = 0,
                            z_slice: int = 0, mipmap_lvl: int = 0) -> None:
        if self.image_format() == VTFImageFormat.IMAGE_FORMAT_RGBA8888:
            return self.image_set_data(data, frame, face, z_slice, mipmap_lvl)
        source_buffer = create_string_buffer(data, len(data))
        width, height, _ = self.compute_mipmap_dimensions(self.image_width(), self.image_height(), 1, mipmap_lvl)
        dest_buffer = create_string_buffer(_vl_image_compute_image_size(width, height, 1, 1, self.image_format()))
        if not _vl_image_convert_from_rgba8888(source_buffer, dest_buffer, width, height, self.image_format()):
            raise VTFException
        _vl_image_set_data(frame, face, z_slice, mipmap_lvl, dest_buffer)

    def image_as(self, dest_format: VTFImageFormat, frame: int = 0, face: int = 0, z_slice: int = 0,
                 mipmap_lvl: int = 0) -> bytes:
        if self.image_format() == dest_format:
            return self.image_get_data(frame, face, z_slice, mipmap_lvl)
        data_pointer = _vl_image_get_data(frame, face, z_slice, mipmap_lvl)
        width, height, _ = self.compute_mipmap_dimensions(self.image_width(), self.image_height(), 1, mipmap_lvl)
        dest_buffer = create_string_buffer(
            _vl_image_compute_image_size(width, height, 1, 1, dest_format)
        )
        if not _vl_image_convert(cast(data_pointer, c_char_p), dest_buffer,
                                 width, height, self.image_format(), dest_format):
            raise VTFException
        return dest_buffer.raw

    def image_from(self, source_format: VTFImageFormat, data: bytes, frame: int = 0, face: int = 0,
                   z_slice: int = 0, mipmap_lvl: int = 0) -> None:
        if self.image_format() == source_format:
            return self.image_set_data(data, frame, face, z_slice, mipmap_lvl)
        source_buffer = create_string_buffer(data, len(data))
        width, height, _ = self.compute_mipmap_dimensions(self.image_width(), self.image_height(), 1, mipmap_lvl)
        dest_buffer = create_string_buffer(_vl_image_compute_image_size(width, height, 1, 1, self.image_format()))
        if not _vl_image_convert(source_buffer, dest_buffer, width, height, source_format, self.image_format()):
            raise VTFException
        _vl_image_set_data(frame, face, z_slice, mipmap_lvl, dest_buffer)
