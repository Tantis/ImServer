// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: im.proto

// This CPP symbol can be defined to use imports that match up to the framework
// imports needed when using CocoaPods.
#if !defined(GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS)
 #define GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS 0
#endif

#if GPB_USE_PROTOBUF_FRAMEWORK_IMPORTS
 #import <Protobuf/GPBProtocolBuffers.h>
#else
 #import "GPBProtocolBuffers.h"
#endif

#if GOOGLE_PROTOBUF_OBJC_VERSION < 30002
#error This file was generated by a newer version of protoc which is incompatible with your Protocol Buffer library sources.
#endif
#if 30002 < GOOGLE_PROTOBUF_OBJC_MIN_SUPPORTED_VERSION
#error This file was generated by an older version of protoc which is incompatible with your Protocol Buffer library sources.
#endif

// @@protoc_insertion_point(imports)

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

CF_EXTERN_C_BEGIN

@class S_C_Send_msg;
@class msgContent;
@class offlineMessage;
@class online;

NS_ASSUME_NONNULL_BEGIN

#pragma mark - Enum IM_HEADER

typedef GPB_ENUM(IM_HEADER) {
  /**
   * Value used if any message's field encounters a value that is not defined
   * by this enum. The message will also have C functions to get/set the rawValue
   * of the field.
   **/
  IM_HEADER_GPBUnrecognizedEnumeratorValue = kGPBUnrecognizedEnumeratorValue,
  /** 第一个值得是0？ */
  IM_HEADER_Firster = 0,

  /** 通信协议 */
  IM_HEADER_CSPing = 268435457,

  /** PING协议 */
  IM_HEADER_SCPing = 268435458,

  /** 错误信息 */
  IM_HEADER_SCError = 272630788,

  /** 通知消息 */
  IM_HEADER_CSInfor = 270533017,

  /** 消息协议 */
  IM_HEADER_SCInfor = 270533120,

  /** 登录 */
  IM_HEADER_SCUserLogined = 1048578,

  /** 发送消息 */
  IM_HEADER_CSSend = 269484033,

  /** 服务器转发消息 */
  IM_HEADER_SCSend = 270532609,

  /** 消息发送反馈 */
  IM_HEADER_SCSendInfo = 270532610,

  /** 发送在线用户 */
  IM_HEADER_SCOnline = 270532865,

  /** 某一个好友上线了 */
  IM_HEADER_SCAddOnline = 270532866,

  /** 某一个好友下线了 */
  IM_HEADER_SCSignOut = 270532867,

  /** 发送离线消息列表 */
  IM_HEADER_SCOfflineMessage = 270532868,
};

GPBEnumDescriptor *IM_HEADER_EnumDescriptor(void);

/**
 * Checks to see if the given value is defined by the enum or was not known at
 * the time this source was generated.
 **/
BOOL IM_HEADER_IsValidValue(int32_t value);

#pragma mark - ImRoot

/**
 * Exposes the extension registry for this file.
 *
 * The base class provides:
 * @code
 *   + (GPBExtensionRegistry *)extensionRegistry;
 * @endcode
 * which is a @c GPBExtensionRegistry that includes all the extensions defined by
 * this file and all files that it depends on.
 **/
@interface ImRoot : GPBRootObject
@end

#pragma mark - C_S_Ping

/**
 * 发送PING协议
 **/
@interface C_S_Ping : GPBMessage

@end

#pragma mark - S_C_Ping

/**
 * 回复PING协议
 **/
@interface S_C_Ping : GPBMessage

@end

#pragma mark - S_C_error

typedef GPB_ENUM(S_C_error_FieldNumber) {
  S_C_error_FieldNumber_Code = 1,
  S_C_error_FieldNumber_Msg = 2,
};

@interface S_C_error : GPBMessage

/** 错误编号 参考status中的状态码 */
@property(nonatomic, readwrite) int32_t code;

/**
 * 401 = 賬號已經被其他用戶頂替
 * 402 = 賬號不允許被登錄
 * 403 = 常規錯誤TOKEN過期，或者不存在
 * 404 = 未定
 * 405 = 未定
 **/
@property(nonatomic, readwrite, copy, null_resettable) NSString *msg;

@end

#pragma mark - C_S_infor

typedef GPB_ENUM(C_S_infor_FieldNumber) {
  C_S_infor_FieldNumber_Code = 1,
  C_S_infor_FieldNumber_Msg = 2,
  C_S_infor_FieldNumber_TargetUserId = 3,
  C_S_infor_FieldNumber_Callback = 4,
};

@interface C_S_infor : GPBMessage

/** 通知编码 自定义 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *code;

/** 通知消息 自定义 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *msg;

/** 通知的目标用户 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *targetUserId;

/** 通知的回调， 自定义 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *callback;

@end

#pragma mark - S_C_infor

typedef GPB_ENUM(S_C_infor_FieldNumber) {
  S_C_infor_FieldNumber_Code = 1,
  S_C_infor_FieldNumber_Msg = 2,
  S_C_infor_FieldNumber_Other = 3,
  S_C_infor_FieldNumber_Callback = 4,
  S_C_infor_FieldNumber_CallbackType = 5,
};

@interface S_C_infor : GPBMessage

/** 信息编号 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *code;

/** 信息文本 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *msg;

/** 其他附带信息 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *other;

/** 回调信息 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *callback;

/** 回调类型 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *callbackType;

@end

#pragma mark - msgContent

typedef GPB_ENUM(msgContent_FieldNumber) {
  msgContent_FieldNumber_Content = 1,
  msgContent_FieldNumber_ImageURL = 2,
  msgContent_FieldNumber_FileURL = 3,
  msgContent_FieldNumber_Time = 4,
  msgContent_FieldNumber_Timestamp = 5,
};

/**
 * 消息类型
 **/
@interface msgContent : GPBMessage

/** 消息内容 客户端自己解析 */
@property(nonatomic, readwrite, copy, null_resettable) NSData *content;

/** 图片地址 客户端自己定义显示格式 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *imageURL;

/** 文件地址或者超链接地址, 客户端自己定义显示格式 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *fileURL;

/** 发送时间 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *time;

/** 发送时间戳 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *timestamp;

@end

#pragma mark - C_S_Send_msg

typedef GPB_ENUM(C_S_Send_msg_FieldNumber) {
  C_S_Send_msg_FieldNumber_MsgId = 1,
  C_S_Send_msg_FieldNumber_UserId = 2,
  C_S_Send_msg_FieldNumber_GroupId = 3,
  C_S_Send_msg_FieldNumber_Type = 4,
  C_S_Send_msg_FieldNumber_ClientMsgId = 5,
  C_S_Send_msg_FieldNumber_SessionId = 6,
  C_S_Send_msg_FieldNumber_Message = 7,
};

/**
 * 发送消息 客户端发往服务器
 **/
@interface C_S_Send_msg : GPBMessage

@property(nonatomic, readwrite, copy, null_resettable) NSString *msgId;

/** 目标用户 -1 = 非用户 */
@property(nonatomic, readwrite) int32_t userId;

/** 目标群组 -1 = 非组 */
@property(nonatomic, readwrite) int32_t groupId;

/** 消息类型 1=文本消息 2=图片消息 3=文件消息 4>=语音消息后面编号可随意使用。都会发送content */
@property(nonatomic, readwrite) uint32_t type;

/** 客户端消息ID */
@property(nonatomic, readwrite, copy, null_resettable) NSString *clientMsgId;

@property(nonatomic, readwrite, copy, null_resettable) NSString *sessionId;

/** 消息内容 */
@property(nonatomic, readwrite, strong, null_resettable) msgContent *message;
/** Test to see if @c message has been set. */
@property(nonatomic, readwrite) BOOL hasMessage;

@end

#pragma mark - S_C_Send_msg

typedef GPB_ENUM(S_C_Send_msg_FieldNumber) {
  S_C_Send_msg_FieldNumber_MsgId = 1,
  S_C_Send_msg_FieldNumber_SessionId = 2,
  S_C_Send_msg_FieldNumber_UserId = 3,
  S_C_Send_msg_FieldNumber_Sender = 4,
  S_C_Send_msg_FieldNumber_TargetGroupId = 5,
  S_C_Send_msg_FieldNumber_TargetUserId = 6,
  S_C_Send_msg_FieldNumber_Type = 7,
  S_C_Send_msg_FieldNumber_ClientMsgId = 8,
  S_C_Send_msg_FieldNumber_State = 9,
  S_C_Send_msg_FieldNumber_Message = 10,
};

/**
 * 发送消息 服务器发往客户端
 **/
@interface S_C_Send_msg : GPBMessage

@property(nonatomic, readwrite, copy, null_resettable) NSString *msgId;

@property(nonatomic, readwrite, copy, null_resettable) NSString *sessionId;

/** 发送者 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *userId;

/** 是否为发送人 0=不是 1=是 */
@property(nonatomic, readwrite) uint32_t sender;

/** 接收者组 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *targetGroupId;

/** 接收者 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *targetUserId;

/** 消息类型 1=文本消息 2=图片消息 3=文件消息 4=语音消息 */
@property(nonatomic, readwrite) uint32_t type;

/** 客户端消息ID */
@property(nonatomic, readwrite, copy, null_resettable) NSString *clientMsgId;

/** 1=时时消息 2=离线消息 */
@property(nonatomic, readwrite) uint32_t state;

/** 消息内容 */
@property(nonatomic, readwrite, strong, null_resettable) msgContent *message;
/** Test to see if @c message has been set. */
@property(nonatomic, readwrite) BOOL hasMessage;

@end

#pragma mark - S_C_Send_Info

typedef GPB_ENUM(S_C_Send_Info_FieldNumber) {
  S_C_Send_Info_FieldNumber_MsgId = 1,
  S_C_Send_Info_FieldNumber_State = 2,
  S_C_Send_Info_FieldNumber_Content = 3,
  S_C_Send_Info_FieldNumber_ClientMsgId = 4,
};

/**
 * 发送消息反馈信息
 **/
@interface S_C_Send_Info : GPBMessage

@property(nonatomic, readwrite, copy, null_resettable) NSString *msgId;

/** 状态 1=发送成功 -1=发送失败 */
@property(nonatomic, readwrite) int32_t state;

/** 失败原因 */
@property(nonatomic, readwrite, copy, null_resettable) NSString *content;

/** 客户端消息ID */
@property(nonatomic, readwrite, copy, null_resettable) NSString *clientMsgId;

@end

#pragma mark - offlineMessage

typedef GPB_ENUM(offlineMessage_FieldNumber) {
  offlineMessage_FieldNumber_UserId = 1,
  offlineMessage_FieldNumber_SessionId = 2,
  offlineMessage_FieldNumber_InfoArray = 3,
};

@interface offlineMessage : GPBMessage

/** 发送者 */
@property(nonatomic, readwrite) int32_t userId;

/** 会话ID */
@property(nonatomic, readwrite, copy, null_resettable) NSString *sessionId;

/** 消息内容 */
@property(nonatomic, readwrite, strong, null_resettable) NSMutableArray<S_C_Send_msg*> *infoArray;
/** The number of items in @c infoArray without causing the array to be created. */
@property(nonatomic, readonly) NSUInteger infoArray_Count;

@end

#pragma mark - S_C_Offline_Message

typedef GPB_ENUM(S_C_Offline_Message_FieldNumber) {
  S_C_Offline_Message_FieldNumber_OfflineArray = 1,
};

/**
 * 发送离线消息
 **/
@interface S_C_Offline_Message : GPBMessage

@property(nonatomic, readwrite, strong, null_resettable) NSMutableArray<offlineMessage*> *offlineArray;
/** The number of items in @c offlineArray without causing the array to be created. */
@property(nonatomic, readonly) NSUInteger offlineArray_Count;

@end

#pragma mark - online

typedef GPB_ENUM(online_FieldNumber) {
  online_FieldNumber_UserId = 1,
  online_FieldNumber_Type = 2,
};

@interface online : GPBMessage

@property(nonatomic, readwrite) int32_t userId;

/** 0=未上线 1=上线 */
@property(nonatomic, readwrite) uint32_t type;

@end

#pragma mark - S_C_Online

typedef GPB_ENUM(S_C_Online_FieldNumber) {
  S_C_Online_FieldNumber_OnlineArray = 1,
};

@interface S_C_Online : GPBMessage

/** 所有好友的状态 */
@property(nonatomic, readwrite, strong, null_resettable) NSMutableArray<online*> *onlineArray;
/** The number of items in @c onlineArray without causing the array to be created. */
@property(nonatomic, readonly) NSUInteger onlineArray_Count;

@end

#pragma mark - S_C_Add_Online

typedef GPB_ENUM(S_C_Add_Online_FieldNumber) {
  S_C_Add_Online_FieldNumber_UserId = 1,
};

@interface S_C_Add_Online : GPBMessage

/** 上线用户 */
@property(nonatomic, readwrite) int32_t userId;

@end

#pragma mark - S_C_Sign_Out

typedef GPB_ENUM(S_C_Sign_Out_FieldNumber) {
  S_C_Sign_Out_FieldNumber_UserId = 1,
};

@interface S_C_Sign_Out : GPBMessage

/** 下线用户 */
@property(nonatomic, readwrite) int32_t userId;

@end

NS_ASSUME_NONNULL_END

CF_EXTERN_C_END

#pragma clang diagnostic pop

// @@protoc_insertion_point(global_scope)
